# ComfyUI-Clip-Text-Encode-Camera-Movements

A CLIP text encoder with **17 cinematic camera movement presets** (dolly, pan, tilt, zoom, orbit and more). Each movement comes in two flavors — **Subject-Aware** (camera follows the subject) and **Natural Movement** (camera moves freely) — plus an **Experimental Mix** mode that combines both for unique compound shots.

---

## ✨ Features

- 🎬 **17 cinematic camera movement presets** — Dolly, Pan, Tilt, Zoom, Orbit, Drone Shot, Handheld and more
- 🎯 **Subject-Aware Camera** — keeps the subject in frame as the camera moves
- 🌍 **Natural Camera Movement** — camera moves freely regardless of the subject
- 🧪 **Experimental Mix** — combine both modes for unpredictable, creative compound shots
- 🎚️ **Concatenate Slider** — blend your prompt with the camera movement (0, 0.5, or 1)
- 👁️ **Live Text Output** — preview the final prompt before generation
- ⚡ Designed for **image-to-video workflows**

---

## 📺 Demo

> 💡 **A note on the demos:** The prompts used in the demo videos are intentionally minimal (e.g., *"a woman next to a window"*). This is on purpose — to showcase the camera movement itself without the prompt influencing or competing with the camera behavior. Each clip plays the **Subject-Aware** version on the left and the **Natural Movement** version on the right, side by side.

### Pan Right
https://github.com/user-attachments/assets/aa1120bd-71cd-4034-b66f-1b8a08ae0f4e

### Pan Left
https://github.com/user-attachments/assets/46267f11-032c-46ef-91f2-af377fe31917

### Tilt Down
https://github.com/user-attachments/assets/8bac3c51-cdfa-45db-adbc-ca553bcbc63e

### Tilt Up
https://github.com/user-attachments/assets/67aa9c7d-39aa-4229-b948-8ae45e15d918

### Dolly In
https://github.com/user-attachments/assets/ae74d7a1-124a-4ab7-9ff3-7950fb567e9e

### Dolly Out
https://github.com/user-attachments/assets/9ae9444d-a790-41df-b99d-fdb079ec9b6a

### Dolly Left
https://github.com/user-attachments/assets/e68e135a-0feb-4b1b-ab92-59d1b83d9734

### Dolly Right
https://github.com/user-attachments/assets/88815c0a-3b71-4662-8e44-8ea722491e14

### Jib Up
https://github.com/user-attachments/assets/b91a0418-bb20-4a70-bccd-99142b43e637

### Jib Down
https://github.com/user-attachments/assets/45efe026-2262-45b2-9188-d3e8f2325cd6

### Orbit Around
https://github.com/user-attachments/assets/b746feac-da0f-42e4-b574-0c5885e0356b

### 360 Roll
https://github.com/user-attachments/assets/758b352f-81d2-465c-8a75-b3e9b458477b

### Zoom In
https://github.com/user-attachments/assets/11e52608-f39d-4ff4-a032-039b3c3928fe

### Zoom Out
https://github.com/user-attachments/assets/a50c1d90-db6b-406f-84ec-6d2d548b4d32

### Handheld
https://github.com/user-attachments/assets/a4eb1dcf-34dc-428e-90ac-7cb9053c9699

### Camera Follows
https://github.com/user-attachments/assets/3a8517f9-6fb9-4126-a448-9755c8812bfb

### Drone Shot
https://github.com/user-attachments/assets/cd899cec-31a7-44ec-8ca5-94d683d19480

---

## 🧪 Experimental Mix Demos

These clips show what happens when you set the **Camera Mode slider to 0.5** and combine a Subject-Aware movement with a Natural Movement at the same time. Results are intentionally unpredictable — sometimes the model produces beautiful compound shots, sometimes something unexpected.

https://github.com/user-attachments/assets/d17bf46b-4acb-48ff-a6b4-2a0b00ecd023

https://github.com/user-attachments/assets/c83bc227-36ac-4ba5-975c-6d24266ad4f9

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
Controls how the user prompt and the camera movement description are combined:

| Value | Clip Text | Camera Movement |
|-------|-----------|-----------------|
| **0** | ✅ Enabled | ❌ Disabled |
| **0.5** | ✅ Enabled | ✅ Enabled |
| **1** | ❌ Disabled | ✅ Enabled |

### Camera Mode slider
The slider label updates dynamically as you change the value:

| Value | Label | Behavior |
|-------|-------|----------|
| **0** | **Subject Aware** | The view repositions to keep the subject in frame at all times |
| **0.5** | **Experimental Mix** 🧪 | Combines both subject-aware and natural movement prompts |
| **1** | **Natural Movement** | The view moves as described, regardless of the subject |

### 🧪 About Experimental Mix
Setting the slider to **0.5** activates Experimental Mix, which sends both the subject-aware and the natural-movement descriptions to the model at the same time. You can pick the same camera movement in both dropdowns, or mix two different ones — for example, **Pan Left** subject-aware + **Tilt Down** natural — to get unique compound shots.

Results vary: sometimes you get amazing hybrid camera behavior, sometimes the model produces something unexpected. It's intentionally open-ended — meant for adventurous experimentation.

### Camera Movements available
`Pan Left`, `Pan Right`, `Tilt Up`, `Tilt Down`, `Dolly In`, `Dolly Out`, `Dolly Left`, `Dolly Right`, `Jib Up`, `Jib Down`, `Orbit Around`, `360 Roll`, `Zoom In`, `Zoom Out`, `Handheld`, `Camera Follows`, `Drone Shot`

---

## 📝 License

MIT — free to use, modify, and share.

---

## 💬 Feedback

Found a bug or have a feature request? [Open an issue](https://github.com/alikonfilms/comfyui_alikonfilms/issues) — happy to hear from you!

Made with ❤️ by [@alikonfilms](https://github.com/alikonfilms)
