/**
 * Clip Text Encode - Camera Movements
 * Web UI Extension for ComfyUI
 *
 * Place this file in: ComfyUI/web/extensions/camera_movement_ui.js
 *
 * Adds color-coded button grids for both:
 *   Row 2 – Subject-Aware camera movements
 *   Row 3 – Body-Fixed camera movements  [NEW]
 */

import { app } from "../../scripts/app.js";

// ---------------------------------------------------------------------------
// Movement definitions shared by both grids
// ---------------------------------------------------------------------------
const MOVEMENTS = [
    { id: "None",           color: "#555555" },
    { id: "Pan Right",      color: "#FF6B6B" },
    { id: "Pan Left",       color: "#FF6B6B" },
    { id: "Tilt Up",        color: "#FF8E72" },
    { id: "Tilt Down",      color: "#FF8E72" },
    { id: "Dolly In",       color: "#6BCB77" },
    { id: "Dolly Out",      color: "#6BCB77" },
    { id: "Dolly Left",     color: "#00D9FF" },
    { id: "Dolly Right",    color: "#00D9FF" },
    { id: "Jib Up",         color: "#9D84B7" },
    { id: "Jib Down",       color: "#9D84B7" },
    { id: "Orbit Around",   color: "#FFD93D" },
    { id: "360 Roll",       color: "#FB5607" },
    { id: "Zoom In",        color: "#4D96FF" },
    { id: "Zoom Out",       color: "#4D96FF" },
    { id: "Static",         color: "#8338EC" },
    { id: "Handheld",       color: "#3A86FF" },
    { id: "Camera Follows", color: "#06A77D" },
    { id: "Drone Shot",     color: "#FF006E" },
];

// ---------------------------------------------------------------------------
// Helper: build a button grid for one dropdown widget
// ---------------------------------------------------------------------------
function buildButtonGrid(node, widgetName, labelText) {
    const wrapper = document.createElement("div");
    wrapper.style.cssText = `
        margin-top: 6px;
        margin-bottom: 2px;
    `;

    // Section label
    const label = document.createElement("div");
    label.textContent = labelText;
    label.style.cssText = `
        font-size: 10px;
        font-weight: bold;
        color: #aaa;
        padding: 2px 4px 4px 4px;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    `;
    wrapper.appendChild(label);

    // Button grid
    const grid = document.createElement("div");
    grid.style.cssText = `
        display: grid;
        grid-template-columns: repeat(6, 1fr);
        gap: 5px;
        padding: 6px;
        background: #222;
        border-radius: 4px;
    `;

    let selectedButton = null;

    MOVEMENTS.forEach(movement => {
        const btn = document.createElement("button");
        btn.textContent = movement.id;
        btn.style.cssText = `
            padding: 10px 4px;
            background-color: #3a3a3a;
            color: #ddd;
            border: 1.5px solid ${movement.color};
            border-radius: 3px;
            cursor: pointer;
            font-size: 10px;
            font-weight: 500;
            transition: all 0.15s ease;
            min-height: 44px;
            text-align: center;
            line-height: 1.2;
            word-break: break-word;
        `;

        btn.onmouseover = () => {
            if (btn !== selectedButton) {
                btn.style.backgroundColor = movement.color + "55";
                btn.style.color = "#fff";
            }
        };

        btn.onmouseout = () => {
            if (btn !== selectedButton) {
                btn.style.backgroundColor = "#3a3a3a";
                btn.style.color = "#ddd";
            }
        };

        btn.onclick = () => {
            // Update the corresponding dropdown widget value
            const widgetIdx = node.widgets.findIndex(w => w.name === widgetName);
            if (widgetIdx !== -1) {
                node.widgets[widgetIdx].value = movement.id;
            }

            // Visual feedback
            if (selectedButton) {
                selectedButton.style.backgroundColor = "#3a3a3a";
                selectedButton.style.color = "#ddd";
            }
            btn.style.backgroundColor = movement.color;
            btn.style.color = "#000";
            btn.style.fontWeight = "bold";
            selectedButton = btn;

            // Trigger graph update
            node.graph?.setDirtyCanvas(true);
        };

        // Highlight the initial value
        const widgetIdx = node.widgets.findIndex(w => w.name === widgetName);
        if (widgetIdx !== -1 && node.widgets[widgetIdx].value === movement.id) {
            btn.style.backgroundColor = movement.color;
            btn.style.color = "#000";
            btn.style.fontWeight = "bold";
            selectedButton = btn;
        }

        grid.appendChild(btn);
    });

    wrapper.appendChild(grid);
    return wrapper;
}

// ---------------------------------------------------------------------------
// Register the extension
// ---------------------------------------------------------------------------
app.registerExtension({
    name: "ComfyUI.ClipTextEncodeCameraMovements",

    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (nodeData.name !== "ClipTextEncodeCameraMovements") return;

        const originalCreated = nodeType.prototype.onNodeCreated;

        nodeType.prototype.onNodeCreated = function () {
            const result = originalCreated ? originalCreated.apply(this) : undefined;

            // Defer until the node's widgets are fully initialised
            setTimeout(() => {
                // ── Row 2 button grid (Subject-Aware) ──────────────────────
                const gridSA = buildButtonGrid(
                    this,
                    "camera_movement_subject_aware",
                    "Row 2 · Subject-Aware (body moves to keep subject visible)"
                );

                // ── Row 3 button grid (Body-Fixed) ─────────────────────────
                const gridBF = buildButtonGrid(
                    this,
                    "camera_movement_body_fixed",
                    "Row 3 · Body-Fixed (body locked, only lens direction changes)"
                );

                // Inject DOM elements into the node's DOM widget area
                // ComfyUI exposes this.domWidget or we fall back to appending to body
                if (this.addDOMWidget) {
                    this.addDOMWidget("button_grid_sa", "div", gridSA, {
                        getValue() { return ""; },
                        setValue() {},
                    });
                    this.addDOMWidget("button_grid_bf", "div", gridBF, {
                        getValue() { return ""; },
                        setValue() {},
                    });
                } else {
                    // Fallback: append after the node element if accessible
                    this.el?.appendChild(gridSA);
                    this.el?.appendChild(gridBF);
                }

                this.setSize(this.computeSize());
            }, 50);

            return result;
        };
    },
});

console.log("[Clip Text Encode - Camera Movements] UI extension loaded.");
