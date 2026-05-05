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
        "The camera performs a smooth horizontal sweep from left to right across the scene. "
        "The subject and environment remain relatively stable while the view continuously moves "
        "rightward, revealing more of what lies to the right and gradually removing the left side "
        "of the frame from view."
    ),

    "Pan Left": (
        "The camera glides horizontally from right to left in a fluid sweeping motion. "
        "The composition shifts gradually to reveal elements on the left side of the scene "
        "while the right portion gradually exits the frame, creating a natural viewing progression."
    ),

    "Tilt Up": (
        "The camera rotates upward on its horizontal axis, transitioning the view from the "
        "subject level toward the sky above. The subject gradually moves down in the frame "
        "while more of the upper atmosphere and sky come into view, creating a sense of "
        "looking upward."
    ),

    "Tilt Down": (
        "The camera tilts downward on its horizontal axis, rotating from the current subject "
        "view toward the ground below. The subject slowly rises in the frame as the camera "
        "reveals more of what lies beneath, creating a downward gazing perspective."
    ),

    "Dolly In": (
        "The camera moves forward toward the subject in a smooth pushing motion, getting "
        "progressively closer. The subject enlarges in the frame while the surrounding "
        "environment gradually falls away, creating an intimate approach that draws the "
        "viewer closer to the focal point."
    ),

    "Dolly Out": (
        "The camera moves backward away from the subject, gradually increasing distance and "
        "creating space. The subject shrinks in the frame as more of the surrounding "
        "environment becomes visible, revealing the broader context and establishing shots."
    ),

    "Dolly Left": (
        "The camera glides laterally to the left while maintaining its forward-facing direction. "
        "The scene slides rightward across the frame as the camera position moves left, "
        "creating a sideways tracking motion that reveals new elements on the left while "
        "pushing the right side away."
    ),

    "Dolly Right": (
        "The camera slides laterally to the right while keeping its facing direction constant. "
        "The environment drifts leftward as the camera moves right, creating a smooth "
        "side-to-side tracking motion that unveils new details on the right side of the composition."
    ),

    "Jib Up": (
        "The camera ascends vertically upward like a crane, maintaining its forward-facing angle "
        "while rising. The subject and foreground remain relatively centered while the camera "
        "gains altitude, revealing more of the overhead space and sky above the subject."
    ),

    "Jib Down": (
        "The camera descends vertically downward like a descending crane, keeping its horizontal "
        "facing direction stable. The camera lowers while the subject remains positioned ahead, "
        "gradually revealing more ground and environmental details below."
    ),

    "Orbit Around": (
        "The camera rotates continuously around the subject in a complete circular orbit, "
        "maintaining a consistent distance and always keeping the subject centered in the frame. "
        "The background and surrounding environment rotate around the stationary subject, "
        "creating a dynamic three-hundred-sixty-degree view."
    ),

    "360 Roll": (
        "The camera rotates completely around its own forward-facing axis in a barrel roll "
        "motion. The subject remains centered while the entire frame spins one full rotation, "
        "creating a swirling effect where the horizon and environment rotate around the "
        "central point."
    ),

    "Zoom In": (
        "The camera lens optically magnifies the subject without the camera moving from its "
        "position. The subject enlarges progressively in the frame while the field of view "
        "narrows, creating a magnified view that draws focus to details without any physical "
        "camera movement."
    ),

    "Zoom Out": (
        "The camera lens optically widens its field of view without moving the camera itself. "
        "The subject appears smaller in the frame as more of the surrounding environment "
        "becomes visible, revealing context and establishing the broader spatial relationship."
    ),

    "Static": (
        "The camera remains locked in a fixed, stationary position throughout the shot. "
        "There is no camera movement of any kind, no pans, tilts, zooms, or adjustments. "
        "The frame stays completely stable and unchanging, maintaining one consistent perspective."
    ),

    "Handheld": (
        "The camera is held by a person, resulting in subtle, organic micro-movements and "
        "natural vibrations. There are minor drifts, gentle sways, and slight jittering that "
        "create an authentic handheld feel without being distractingly shaky, suggesting a "
        "documentary or intimate cinematic approach."
    ),

    "Camera Follows": (
        "The camera smoothly tracks alongside and follows the subject as it moves through "
        "the environment. The subject remains consistently positioned in the frame as the "
        "camera moves in sync with the subject's motion, creating a dynamic tracking shot "
        "that maintains focus on the moving subject."
    ),

    "Drone Shot": (
        "The camera mounted on an aerial drone moves upward and backward simultaneously, "
        "gaining altitude and distance from the subject. The perspective shifts from a "
        "frontal view to an elevated aerial angle, revealing the expansive landscape and "
        "contextual environment from above."
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
        "The camera body is completely stationary and locked in place. Only the camera head "
        "rotates horizontally to the right, sweeping the lens from the current angle toward "
        "the right side. The pivot point stays fixed; no lateral translation occurs. "
        "The field of view pans purely from left to right as if the camera were mounted on "
        "a fixed tripod head rotating on its vertical axis."
    ),

    "Pan Left": (
        "The camera body remains perfectly still and fixed in position. The camera head "
        "rotates horizontally to the left, turning the lens from its current angle toward "
        "the left side. Pure rotational pan with zero lateral movement; the tripod or mount "
        "does not move. The field of view sweeps from right to left around the fixed vertical axis."
    ),

    "Tilt Down": (
        "The camera body is completely immobile and anchored in place. The camera head tilts "
        "downward on its horizontal axis, rotating the lens from the current level toward the "
        "ground. Starting at face or mid-body level, the view descends from head to torso to "
        "waist to feet, following the body downward. No vertical body movement occurs whatsoever; "
        "only the lens rotates down on the fixed tilt axis. The subject fills the frame "
        "top-to-bottom as the view descends steadily."
    ),

    "Tilt Up": (
        "The camera body stays completely fixed and does not rise or lower at all. The camera "
        "head tilts upward on its horizontal axis, rotating the lens from the current level "
        "toward the sky. Starting near the ground or subject base, the view ascends upward "
        "revealing more of the subject from feet to face to the sky above. Pure rotational "
        "tilt with no vertical body translation whatsoever."
    ),

    "Dolly In": (
        "The camera body moves forward along the ground plane directly toward the subject, "
        "closing the physical distance. The lens direction stays constant and aimed at the "
        "subject throughout. The subject grows larger due to physical proximity, not optical "
        "zoom. Depth-of-field shifts noticeably as the camera approaches. Background "
        "compression increases as the camera physically advances forward."
    ),

    "Dolly Out": (
        "The camera body moves backward along the ground plane, increasing the physical "
        "distance from the subject. The lens remains aimed in the same direction as the "
        "camera retreats. The subject shrinks in the frame due to actual distance increase, "
        "not zoom. The environment around the subject expands into view as the camera "
        "physically withdraws."
    ),

    "Dolly Left": (
        "The camera body slides purely laterally to the left along the ground, maintaining "
        "its forward-facing direction without rotating. The camera does not pan or turn; "
        "it only translates sideways. The subject shifts toward the right side of the frame "
        "as the camera moves left. Strong parallax effect: near objects move faster across "
        "frame than far objects, revealing scene depth."
    ),

    "Dolly Right": (
        "The camera body slides purely laterally to the right along the ground without any "
        "rotation or turning. The lens stays aimed in the same forward direction throughout. "
        "The subject drifts toward the left side of the frame as the camera translates right. "
        "Classic parallax tracking: foreground elements move faster than background, "
        "emphasizing scene depth."
    ),

    "Jib Up": (
        "The camera body rises vertically upward while its lens angle remains fixed and does "
        "not compensate by tilting down. The camera gains height and the horizon rises in "
        "frame, revealing more sky and less ground. The subject gradually moves lower in the "
        "frame as the camera ascends, eventually showing a top-down overhead perspective "
        "without any lens re-aiming."
    ),

    "Jib Down": (
        "The camera body descends vertically downward while keeping its lens angle constant "
        "and not tilting up to compensate. As the camera lowers, the horizon descends in "
        "frame and more ground becomes visible. The subject gradually rises in the frame as "
        "the camera drops, eventually revealing a worm's-eye low-angle view without any "
        "lens adjustment."
    ),

    "Orbit Around": (
        "The camera body travels in a perfect circle around a fixed central point, maintaining "
        "a constant radius. The lens is always aimed inward at the center point but the body "
        "physically moves around it. This is a pure translation orbit: the camera position "
        "moves through an arc while the lens rotates to maintain aim. The subject at center "
        "is seen from progressively different angles as the camera circles."
    ),

    "360 Roll": (
        "The camera body rotates around its own optical axis, performing a complete barrel "
        "roll. The lens direction stays pointed the same way but the camera itself rotates "
        "360 degrees around that axis. The horizon spins from level to tilted to inverted "
        "and back to level. The center of frame stays consistent while everything rotates "
        "around it."
    ),

    "Zoom In": (
        "The camera body stays completely fixed in position. The focal length of the lens "
        "is optically increased, magnifying the view. This is a pure lens operation with "
        "zero physical camera movement. The subject appears larger due to optical magnification "
        "only. Background compression increases and depth of field narrows as focal length "
        "increases. Distinct from dolly-in as no spatial translation occurs."
    ),

    "Zoom Out": (
        "The camera body remains entirely stationary in space. The focal length of the lens "
        "is optically decreased, widening the field of view. Pure lens operation, no physical "
        "movement of the camera. The subject appears smaller as the widening view encompasses "
        "more of the scene. Background expands into frame. Distinct from dolly-out as the "
        "camera does not physically move backward."
    ),

    "Static": (
        "The camera body and lens are both completely locked. There is absolutely no movement "
        "of any kind: no pan, no tilt, no zoom, no translation, no rotation. The frame is "
        "perfectly still as if the camera were bolted in concrete. Every element in the scene "
        "stays at its exact pixel position for the entire shot."
    ),

    "Handheld": (
        "The camera is physically held by a human operator, introducing subtle organic "
        "imperfections: micro-tremors from breathing and heartbeat, gentle sways from weight "
        "shifting, occasional small drifts and micro-corrections. These movements are small "
        "and human-scale. The camera does not track or follow the subject intentionally; "
        "any subject framing changes are incidental to the natural body movement of the operator."
    ),

    "Camera Follows": (
        "The camera body physically moves through space to track and follow the subject as it "
        "moves. The camera translates laterally, forward, or backward to keep pace with the "
        "subject. The lens direction adjusts as needed to maintain aim on the moving subject. "
        "This is a physical tracking movement where the camera body travels alongside "
        "the subject through the environment."
    ),

    "Drone Shot": (
        "The camera is mounted on an aerial drone that rises straight up vertically from its "
        "current position. The lens points downward or forward and does not change angle as "
        "the drone ascends. The ground recedes below and the horizon expands outward as "
        "altitude increases. The drone body rises while the lens direction stays fixed "
        "relative to the drone body, revealing the landscape from an increasingly aerial perspective."
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
                "camera_movement_subject_aware": (subject_aware_list, {
                    "default": "None",
                }),
                # Row 3 – body-fixed movement  [NEW]
                "camera_movement_body_fixed": (body_fixed_list, {
                    "default": "None",
                }),
                # Blend between Row-2 and Row-3 prompts  [NEW]
                # 0.0 = 100% Row-2 (subject-aware only)
                # 1.0 = 100% Row-3 (body-fixed only)
                # 0.5 = both descriptions included equally
                "row_mix": ("FLOAT", {
                    "default": 0.5,
                    "min": 0.0,
                    "max": 1.0,
                    "step": 0.01,
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
                    "step": 0.01,
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

        # Pure Row-2
        if row_mix == 0.0:
            return sa_prompt

        # Pure Row-3
        if row_mix == 1.0:
            return bf_prompt

        # Blend: include both descriptions.
        # Order by dominant side so the stronger description leads.
        if row_mix <= 0.5:
            # Subject-aware is dominant → put it first
            return f"{sa_prompt} {bf_prompt}"
        else:
            # Body-fixed is dominant → put it first
            return f"{bf_prompt} {sa_prompt}"

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
    def encode(
        self,
        clip,
        text: str,
        camera_movement_subject_aware: str,
        camera_movement_body_fixed: str,
        row_mix: float,
        concatenate: float,
    ):
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
