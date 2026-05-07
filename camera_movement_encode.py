"""
Clip Text Encode - Camera Movements Node for ComfyUI

Features:
- Row 1: Text input field
- Row 2: Subject-Aware camera movements dropdown
  → Camera body adjusts to always keep subject visible
  → e.g. "Tilt Down" = camera body rises + tilts down, subject stays in frame
- Row 3: Body-Fixed camera movements dropdown  [NEW]
  → Camera body is completely fixed; only lens/target direction changes
  → e.g. "Tilt Down" = lens rotates downward from head to feet, body never moves
- Concatenate Slider: Blends user text with combined camera movement prompt (0.0–1.0)
- Row Mix Slider: Blends between Row 2 and Row 3 movement styles (0.0=Row2, 1.0=Row3) [NEW]
- CONDITIONING output → KSampler positive/negative
- TEXT output → preview the final prompt
"""

from typing import Tuple


# ---------------------------------------------------------------------------
# Row 2: Subject-Aware Camera Movements
# The camera body repositions itself in 3D space to keep the subject visible.
# Think of a camera operator tracking an actor – body moves with the shot.
# ---------------------------------------------------------------------------
SUBJECT_AWARE_MOVEMENTS = {
    "None": "",

    "Pan Right": (
        "The view stays anchored on the subject as the perspective rotates horizontally to the right, "
        "sweeping the scene from left to right across the frame. The subject remains centered and clearly "
        "visible at all times while the surrounding environment shifts behind them, with new background "
        "elements coming into view on the right as the left side gradually rotates out. The horizon stays "
        "level throughout."
    ),

    "Pan Left": (
        "The view stays anchored on the subject as the perspective rotates horizontally to the left, "
        "sweeping the scene from right to left across the frame. The subject remains centered and clearly "
        "visible at all times while the surrounding environment shifts behind them, with new background "
        "elements coming into view on the left as the right side gradually rotates out. The horizon stays "
        "level throughout."
    ),

    "Tilt Up": (
        "The view stays in one position while the perspective rotates upward, with the subject staying "
        "centered in frame. The view starts at the subject's level and gradually tilts up to reveal what "
        "is above, sweeping from the subject's level toward the sky."
    ),

    "Tilt Down": (
        "The view stays in one position while the perspective rotates downward, with the subject staying "
        "centered in frame. The view starts at the subject's level and gradually tilts down to reveal what "
        "is below, sweeping from the subject's level toward the ground."
    ),

    "Dolly In": (
        "The view moves smoothly forward through the scene, getting closer to the subject. The subject "
        "stays centered and grows larger in the frame as the view advances toward it, while the surroundings "
        "expand outward past the edges of the frame. The sense of depth deepens as the view glides forward."
    ),

    "Dolly Out": (
        "The view moves smoothly backward through the scene, pulling away from the subject. The subject "
        "stays centered and shrinks in the frame as the view retreats, while more of the surrounding "
        "environment gradually comes into the frame. The sense of space opens up as the view glides backward."
    ),

    "Dolly Left": (
        "The view slides smoothly to the left while continuing to face the same forward direction, "
        "keeping the subject framed as it tracks alongside. The environment drifts to the right as the "
        "view moves left, with foreground elements shifting faster than the background to reveal a "
        "sense of depth."
    ),

    "Dolly Right": (
        "The view slides smoothly to the right while continuing to face the same forward direction, "
        "keeping the subject framed as it tracks alongside. The environment drifts to the left as the "
        "view moves right, with foreground elements shifting faster than the background to reveal a "
        "sense of depth."
    ),

    "Jib Up": (
        "The view rises smoothly upward through space while continuing to face the same direction, "
        "with the subject staying in frame. The horizon rises in the frame, revealing more sky and less "
        "ground. The subject stays in its original position and gradually moves lower in the frame as "
        "the view ascends, eventually showing a top-down overhead view."
    ),

    "Jib Down": (
        "The view descends smoothly downward through space while continuing to face the same direction, "
        "with the subject staying in frame. The horizon drops in the frame and more ground becomes "
        "visible. The subject stays in its original position and gradually rises in the frame as the "
        "view lowers, eventually revealing a low-angle ground-level view."
    ),

    "Orbit Around": (
        "The view travels in a wide curving arc around the subject, sweeping at least halfway around "
        "from one side to the other. The subject stays centered in the frame while the background "
        "shifts dramatically behind them, revealing the subject from clearly different angles as the view "
        "glides around. The motion is smooth and continuous, like circling around a statue to see it from "
        "multiple sides."
    ),

    "360 Roll": (
        "The entire scene rotates rapidly around the center of the frame, completing one full clockwise "
        "revolution while the subject stays centered throughout. The horizon tilts sharply to the right, "
        "becomes fully vertical, then completely inverts upside down with the sky now below and the ground "
        "above, then continues rotating until vertical on the left side, and finally rights itself back to "
        "level. The full inversion in the middle of the motion is essential — the scene is clearly flipped "
        "upside down halfway through."
    ),

    "Zoom In": (
        "The view stays completely fixed in position while gradually pushing in closer to the subject, "
        "smoothly and continuously throughout the entire shot. The subject stays centered and grows steadily "
        "larger in the frame at a slow even pace, while the surrounding scene gradually disappears past the "
        "edges. There is no movement through space — only a slow continuous zoom that progresses smoothly "
        "from start to finish without any jumps or steps."
    ),

    "Zoom Out": (
        "The view stays entirely stationary in position while gradually pulling back from the subject, "
        "smoothly and continuously throughout the entire shot. The subject stays centered and grows steadily "
        "smaller in the frame at a slow even pace, while more of the surrounding scene gradually comes into "
        "view from the edges. There is no movement through space — only a slow continuous zoom out that "
        "progresses smoothly from start to finish without any jumps or steps."
    ),

    "Handheld": (
        "The view has subtle organic movement, as if held by a person walking gently or breathing, while "
        "keeping the subject roughly framed. Small natural sways, micro-tremors, and gentle drifts give the "
        "frame a human, lived-in quality. These movements are small and natural, not deliberate tracking."
    ),

    "Camera Follows": (
        "The view moves smoothly through space to keep up with the subject as it moves. The view glides "
        "alongside, behind, or in front of the subject, adjusting its direction as needed to keep the "
        "subject centered in the frame. The motion of the view matches the pace and direction of the subject."
    ),

    "Drone Shot": (
        "The view rises smoothly straight up into the air, gaining altitude while keeping the subject "
        "framed below. The ground recedes and the horizon opens up wider as the view climbs higher. The "
        "subject stays in its original position and the scene is revealed from an increasingly aerial "
        "vantage point, with the landscape spreading out below."
    ),
}


# ---------------------------------------------------------------------------
# Row 3: Body-Fixed Camera Movements  [NEW]
# The camera BODY is completely stationary – bolted to a tripod or head mount.
# Only the lens direction / framing target changes in space.
# Think of a security camera or a tripod-mounted head that can only rotate,
# never translate in space.
# ---------------------------------------------------------------------------
BODY_FIXED_MOVEMENTS = {
    "None": "",

    "Pan Right": (
        "The view stays fixed in one position while the perspective rotates horizontally to the right. "
        "The scene sweeps from left to right across the frame, revealing what was previously off-screen "
        "on the right side as elements gradually exit on the left. The horizon stays level throughout."
    ),

    "Pan Left": (
        "The view stays fixed in one position while the perspective rotates horizontally to the left. "
        "The scene sweeps from right to left across the frame, revealing what was previously off-screen "
        "on the left side as elements gradually exit on the right. The horizon stays level throughout."
    ),

    "Tilt Down": (
        "The view stays fixed in one position while the perspective rotates downward. The view starts at "
        "upper or eye level and gradually tilts down to reveal what is below, sweeping from above toward "
        "the ground."
    ),

    "Tilt Up": (
        "The view stays fixed in one position while the perspective rotates upward. The view starts at "
        "lower or ground level and gradually tilts up to reveal what is above, sweeping from below toward "
        "the sky."
    ),

    "Dolly In": (
        "The view moves smoothly forward through the scene, getting closer to the subject. The subject "
        "grows larger in the frame as the view advances toward it, while the surroundings expand outward "
        "past the edges of the frame. The sense of depth deepens as the view glides forward."
    ),

    "Dolly Out": (
        "The view moves smoothly backward through the scene, pulling away from the subject. The subject "
        "shrinks in the frame as the view retreats, while more of the surrounding environment gradually "
        "comes into the frame. The sense of space opens up as the view glides backward."
    ),

    "Dolly Left": (
        "The view moves smoothly to the left while continuing to face the same forward direction. "
        "Everything in the scene appears to slide to the right as the view glides leftward. Objects "
        "close to the foreground shift across the frame faster than distant objects, creating a sense "
        "of depth and lateral motion."
    ),

    "Dolly Right": (
        "The view moves smoothly to the right while continuing to face the same forward direction. "
        "Everything in the scene appears to slide to the left as the view glides rightward. Objects "
        "close to the foreground shift across the frame faster than distant objects, creating a sense "
        "of depth and lateral motion."
    ),

    "Jib Up": (
        "The view rises smoothly upward through space while continuing to face the same direction. "
        "The horizon rises in the frame, revealing more sky and less ground. The subject gradually "
        "moves lower in the frame as the view ascends, eventually showing a top-down overhead view."
    ),

    "Jib Down": (
        "The view descends smoothly downward through space while continuing to face the same direction. "
        "The horizon drops in the frame and more ground becomes visible. The subject gradually rises in "
        "the frame as the view lowers, eventually revealing a low-angle ground-level view."
    ),

    "Orbit Around": (
        "The view travels in a wide curving arc around the subject, sweeping at least halfway around "
        "from one side to the other. The subject stays roughly centered in the frame while the background "
        "shifts dramatically behind them, revealing the subject from clearly different angles as the view "
        "glides around. The motion is smooth and continuous, like circling around a statue to see it from "
        "multiple sides."
    ),

    "360 Roll": (
        "The entire scene rotates rapidly around the center of the frame, completing one full clockwise "
        "revolution. The horizon tilts sharply to the right, becomes fully vertical, then completely "
        "inverts upside down with the sky now below and the ground above, then continues rotating until "
        "vertical on the left side, and finally rights itself back to level. The full inversion in the "
        "middle of the motion is essential — the scene is clearly flipped upside down halfway through."
    ),

    "Zoom In": (
        "The view stays completely fixed in position while gradually pushing in closer to the subject, "
        "smoothly and continuously throughout the entire shot. The subject grows steadily larger in the "
        "frame at a slow even pace, while the surrounding scene gradually disappears past the edges. "
        "There is no movement through space — only a slow continuous zoom that progresses smoothly from "
        "start to finish without any jumps or steps."
    ),

    "Zoom Out": (
        "The view stays entirely stationary in position while gradually pulling back from the subject, "
        "smoothly and continuously throughout the entire shot. The subject grows steadily smaller in the "
        "frame at a slow even pace, while more of the surrounding scene gradually comes into view from "
        "the edges. There is no movement through space — only a slow continuous zoom out that progresses "
        "smoothly from start to finish without any jumps or steps."
    ),

    "Handheld": (
        "The view has subtle organic movement, as if held by a person walking gently or breathing. "
        "Small natural sways, micro-tremors, and gentle drifts give the frame a human, lived-in quality. "
        "These movements are small and natural, not deliberate tracking. The framing wobbles slightly "
        "without following the subject intentionally."
    ),

    "Camera Follows": (
        "The view moves smoothly through space to keep up with the subject as it moves. The view glides "
        "alongside, behind, or in front of the subject, adjusting its direction as needed to keep the "
        "subject in frame. The motion of the view matches the pace and direction of the subject."
    ),

    "Drone Shot": (
        "The view rises smoothly straight up into the air, gaining altitude. The ground recedes below "
        "and the horizon opens up wider as the view climbs higher. The scene is revealed from an "
        "increasingly aerial vantage point, with the landscape spreading out below."
    ),
}


class ClipTextEncodeCameraMovements:
    """
    Clip Text Encode - Camera Movements

    Row 1 : Text prompt input
    Row 2 : Subject-Aware camera movement dropdown
            (camera body moves to keep subject always visible)
    Row 3 : Body-Fixed camera movement dropdown  [NEW]
            (camera body is locked; only lens/target direction changes)
    Row Mix Slider  : blend between Row-2 and Row-3 style (0.0 = Row2, 1.0 = Row3)  [NEW]
    Concatenate Slider : mix between user text and the combined camera prompt
    """

    @classmethod
    def INPUT_TYPES(cls):
        subject_aware_list = list(SUBJECT_AWARE_MOVEMENTS.keys())
        body_fixed_list = list(BODY_FIXED_MOVEMENTS.keys())

        return {
            "required": {
                "clip": ("CLIP",),
                # Row 1 – user text
                "text": ("STRING", {
                    "multiline": True,
                    "default": "a person standing in a field",
                }),
                # Row 2 – subject-aware movement
                "Camera (0) (Subject Aware)": (subject_aware_list, {
                    "default": "None",
                }),
                # Row 3 – body-fixed movement  [NEW]
                "Camera (1) (Natural Movement)": (body_fixed_list, {
                    "default": "None",
                }),
                # Choose Camera (Row 2 vs Row 3)
                # 0.0   = Subject-Aware only (Camera 0)
                # 1.0   = Natural Movement only (Camera 1)
                # 0.5   = Experimental — both combined (subject-aware first)
                "Choose Camera": ("FLOAT", {
                    "default": 0.0,
                    "min": 0.0,
                    "max": 1.0,
                    "step": 0.5,
                    "display": "slider",
                }),
                # Blend between user text and combined camera prompt
                # 0.0 = 100% user text only
                # 1.0 = 100% camera prompt only
                # 0.5 = both
                "concatenate": ("FLOAT", {
                    "default": 0.5,
                    "min": 0.0,
                    "max": 1.0,
                    "step": 0.5,
                    "display": "slider",
                }),
            },
        }

    RETURN_TYPES = ("CONDITIONING", "STRING")
    RETURN_NAMES = ("CONDITIONING", "TEXT")
    FUNCTION = "encode"
    CATEGORY = "conditioning/text"

    # ------------------------------------------------------------------
    def _build_camera_prompt(
        self,
        subject_aware_key: str,
        body_fixed_key: str,
        row_mix: float,
    ) -> str:
        """
        Compose a camera prompt by blending Row-2 and Row-3 descriptions.

        row_mix = 0.0  → only subject-aware (Row 2)
        row_mix = 1.0  → only body-fixed    (Row 3)
        in between     → both descriptions included, ordered by dominant weight
        """
        sa_prompt = SUBJECT_AWARE_MOVEMENTS.get(subject_aware_key, "").strip()
        bf_prompt = BODY_FIXED_MOVEMENTS.get(body_fixed_key, "").strip()

        # Nothing selected in either row
        if not sa_prompt and not bf_prompt:
            return ""

        # Only one row has content → return it regardless of slider
        if not sa_prompt:
            return bf_prompt
        if not bf_prompt:
            return sa_prompt

        # Pure Row-2 (Subject-Aware only)
        if row_mix == 0.0:
            return sa_prompt

        # Pure Row-3 (Natural Movement only)
        if row_mix == 1.0:
            return bf_prompt

        # 0.5 = Experimental mode — both combined, subject-aware first
        return f"{sa_prompt} {bf_prompt}"

    # ------------------------------------------------------------------
    def _build_full_prompt(
        self,
        text: str,
        camera_prompt: str,
        concatenate: float,
    ) -> str:
        """
        Blend the user's text with the camera prompt according to `concatenate`.

        concatenate = 0.0  → only user text
        concatenate = 1.0  → only camera prompt
        in between         → both combined
        """
        text = text.strip()
        camera_prompt = camera_prompt.strip()

        if not camera_prompt:
            return text
        if not text:
            return camera_prompt

        if concatenate == 0.0:
            return text
        if concatenate == 1.0:
            return camera_prompt

        # For values in between, concatenate both.
        # Dominant side leads.
        if concatenate <= 0.5:
            # Text dominant
            return f"{text}, {camera_prompt}"
        else:
            # Camera dominant
            return f"{camera_prompt}, {text}"

    # ------------------------------------------------------------------
    def encode(self, clip, text, concatenate, **kwargs):
        # Extract the spaced/parenthesized parameter names from kwargs
        camera_movement_subject_aware = kwargs.get("Camera (0) (Subject Aware)", "None")
        camera_movement_body_fixed = kwargs.get("Camera (1) (Natural Movement)", "None")
        row_mix = kwargs.get("Choose Camera", 0.0)

        # 1. Build blended camera prompt from Row 2 + Row 3
        camera_prompt = self._build_camera_prompt(
            camera_movement_subject_aware,
            camera_movement_body_fixed,
            row_mix,
        )

        # 2. Blend user text with camera prompt
        full_text = self._build_full_prompt(text, camera_prompt, concatenate)

        # 3. CLIP encode
        tokens = clip.tokenize(full_text)
        cond, pooled = clip.encode_from_tokens(tokens, return_pooled=True)

        # 4. Standard ComfyUI conditioning format
        output = [[cond, {"pooled_output": pooled}]]

        return (output, full_text)


# ---------------------------------------------------------------------------
# ComfyUI registration
# ---------------------------------------------------------------------------
NODE_CLASS_MAPPINGS = {
    "ClipTextEncodeCameraMovements": ClipTextEncodeCameraMovements,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ClipTextEncodeCameraMovements": "Clip Text Encode - Camera Movements",
}
