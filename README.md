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
 
### Pan Right
https://github.com/user-attachments/assets/c3892f65-2ec5-4c46-af32-f7f7dcb3670c
 
### Pan Left
https://github.com/user-attachments/assets/772e2a89-f7af-47ec-af5e-21fedeaa6d14
 
### Tilt Down
https://github.com/user-attachments/assets/fb69cf0f-de43-4516-bb95-78b13d4bae63
 
### Tilt Up
https://github.com/user-attachments/assets/91bafd94-c76e-4b40-92ad-a73c3dfb1b79
 
### Dolly In
https://github.com/user-attachments/assets/1191709a-0086-4beb-88a3-bfdef79d7808
 
### Dolly Out
https://github.com/user-attachments/assets/5538fce8-7080-49c4-8f8a-312ddf1ee4ac
 
### Dolly Left
https://github.com/user-attachments/assets/738a565c-56fe-4b40-96cd-db9640d5996c
 
### Dolly Right
https://github.com/user-attachments/assets/b737677b-a2aa-4f1c-a41c-f6dc34477756
 
### Jib Up
https://github.com/user-attachments/assets/e34c3b08-3e81-4402-807c-a310a4acb133
 
### Jib Down
https://github.com/user-attachments/assets/492fb8b7-5737-4410-93a8-9a24f8f8a064
 
### Orbit Around
https://github.com/user-attachments/assets/d94ec9fd-177d-4ed9-b5fd-9bf5b94125ab
 
### 360 Roll
https://github.com/user-attachments/assets/a6441748-da09-4baf-9b55-df65b16570ba
 
### Zoom In
https://github.com/user-attachments/assets/9e518f12-97b9-42c4-827a-4954a2020d4e
 
### Zoom Out
https://github.com/user-attachments/assets/d7d06eea-2a52-487d-890e-539f89657e33
 
### Static
https://github.com/user-attachments/assets/a5152434-35b9-4013-b2ae-faf9565d12f4
 
### Handheld
https://github.com/user-attachments/assets/30cbdded-c555-4766-aa43-331d1d524e25
 
### Camera Follows
https://github.com/user-attachments/assets/578ba99c-a959-4eea-bd83-cd78eb20b805
 
### Drone Shot
https://github.com/user-attachments/assets/09e15e52-d313-4faf-bcc2-c1e36c325579
 
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
 
## 📝 License
 
MIT — free to use, modify, and share.
 
---
 
## 💬 Feedback
 
Found a bug or have a feature request? [Open an issue](https://github.com/alikonfilms/comfyui_alikonfilms/issues) — happy to hear from you!
 
Made with ❤️ by [@alikonfilms](https://github.com/alikonfilms)
