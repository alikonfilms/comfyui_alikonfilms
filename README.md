# Clip Text Encode - Camera Movements

A CLIP text encoder with **18 cinematic camera movement presets** (dolly, pan, tilt, zoom, orbit and more). Subject-aware and natural-movement modes, with a blend slider to mix your prompt with camera movements, and a live text output to preview the final prompt.

---

## ✨ Features

- 🎬 **18 cinematic camera movement presets** — Dolly, Pan, Tilt, Zoom, Orbit, Drone Shot, Handheld and more
- 🎯 **Subject-Aware Camera** — keeps the subject in frame as the camera moves
- 🌍 **Natural Camera Movement** — camera moves freely regardless of the subject
- 🎚️ **Concatenate Slider** — blend your prompt with the camera movement (0, 0.5, or 1)
- 👁️ **Live Text Output** — preview the final prompt before generation
- ⚡ Designed for **image-to-video workflows**

---

## 📺 Demo



https://github.com/user-attachments/assets/358d1b33-df01-49fe-a242-9477bb2d8a5a

https://github.com/user-attachments/assets/25b4a72c-b4b4-4a2d-9fac-91480583ac43

https://github.com/user-attachments/assets/79cc489f-5e4b-48e2-9a35-566fa7607ab5

https://github.com/user-attachments/assets/f05a6e75-03fa-48ba-b9fe-a4d36c6c3c5a





---

## 🛠️ Installation

### Option 1 — ComfyUI-Manager (recommended)
1. Open ComfyUI-Manager
2. Click **Custom Nodes Manager**
3. Search for `comfyui_alikonfilms`
4. Click **Install**
5. Restart ComfyUI

### Option 2 — Manual install
1. Navigate to your `ComfyUI/custom_nodes/` folder
2. Clone this repo:
   ```
   git clone https://github.com/alikonfilms/comfyui_alikonfilms.git
   ```
3. Restart ComfyUI

Also available on the [Comfy Registry](https://registry.comfy.org/publishers/alikonfilms).

---

## 🎛️ How to Use

### Concatenate slider
| Value | Clip Text | Camera Movement |
|-------|-----------|-----------------|
| **0** | ✅ Enabled | ❌ Disabled |
| **0.5** | ✅ Enabled | ✅ Enabled |
| **1** | ❌ Disabled | ✅ Enabled |

### Choose Camera slider
Pick which camera mode to use:

- **(0) Subject-Aware** — the camera repositions to keep the subject in frame at all times
- **(1) Natural Movement** — the camera moves as described regardless of where the subject is

### Camera Movements available
`Pan Left`, `Pan Right`, `Tilt Up`, `Tilt Down`, `Dolly In`, `Dolly Out`, `Dolly Left`, `Dolly Right`, `Jib Up`, `Jib Down`, `Orbit Around`, `360 Roll`, `Zoom In`, `Zoom Out`, `Static`, `Handheld`, `Camera Follows`, `Drone Shot`

---

## 📷 Examples

<!-- Drop screenshots or short clips of the node in action here -->

---

## 📝 License

MIT — free to use, modify, and share.

---

## 💬 Feedback

Found a bug or have a feature request? [Open an issue](https://github.com/alikonfilms/comfyui_alikonfilms/issues) — happy to hear from you!

Made with ❤️ by [@alikonfilms](https://github.com/alikonfilms)
