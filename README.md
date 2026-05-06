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

https://github.com/user-attachments/assets/c3892f65-2ec5-4c46-af32-f7f7dcb3670c

https://github.com/user-attachments/assets/772e2a89-f7af-47ec-af5e-21fedeaa6d14

https://github.com/user-attachments/assets/fb69cf0f-de43-4516-bb95-78b13d4bae63

https://github.com/user-attachments/assets/91bafd94-c76e-4b40-92ad-a73c3dfb1b79

https://github.com/user-attachments/assets/1191709a-0086-4beb-88a3-bfdef79d7808

https://github.com/user-attachments/assets/5538fce8-7080-49c4-8f8a-312ddf1ee4ac

https://github.com/user-attachments/assets/738a565c-56fe-4b40-96cd-db9640d5996c

https://github.com/user-attachments/assets/b737677b-a2aa-4f1c-a41c-f6dc34477756

https://github.com/user-attachments/assets/e34c3b08-3e81-4402-807c-a310a4acb133

https://github.com/user-attachments/assets/bdbed970-5484-404f-9467-9d354656158b

https://github.com/user-attachments/assets/d94ec9fd-177d-4ed9-b5fd-9bf5b94125ab



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
