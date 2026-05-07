/**
 * Clip Text Encode - Camera Movements
 * Web UI Extension for ComfyUI
 *
 * Snaps concatenate slider to 0, 0.5, 1.
 * Snaps "Choose Camera" slider to 0, 0.5, 1 with dynamic label.
 */

import { app } from "../../scripts/app.js";

app.registerExtension({
    name: "ComfyUI.ClipTextEncodeCameraMovements",

    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (nodeData.name !== "ClipTextEncodeCameraMovements") return;

        const originalCreated = nodeType.prototype.onNodeCreated;

        nodeType.prototype.onNodeCreated = function () {
            const result = originalCreated ? originalCreated.apply(this) : undefined;

            setTimeout(() => {
                const snapTriple = (v) => {
                    if (v <= 0.25) return 0.0;
                    if (v >= 0.75) return 1.0;
                    return 0.5;
                };

                // ── Snap concatenate slider ────────────────────────────────
                const concatWidget = this.widgets.find(w => w.name === "concatenate");
                if (concatWidget) {
                    let cv = snapTriple(concatWidget.value);
                    Object.defineProperty(concatWidget, "value", {
                        get() { return cv; },
                        set(v) { cv = snapTriple(v); },
                        configurable: true,
                    });
                }

                // ── "Choose Camera" slider with dynamic label ──────────────
                const rowMixWidget = this.widgets.find(w => w.name === "Choose Camera");
                if (rowMixWidget) {
                    let internalValue = snapTriple(rowMixWidget.value);

                    const labelFor = (v) => {
                        if (v === 0.0) return "Subject Aware";
                        if (v === 1.0) return "Natural Movement";
                        return "Experimental Mix";
                    };

                    Object.defineProperty(rowMixWidget, "value", {
                        get() { return internalValue; },
                        set(v) {
                            internalValue = snapTriple(v);
                            rowMixWidget.label = labelFor(internalValue);
                        },
                        configurable: true,
                    });

                    // Set initial label
                    rowMixWidget.label = labelFor(internalValue);
                }

                this.setSize(this.computeSize());
            }, 50);

            return result;
        };
    },
});

console.log("[Clip Text Encode - Camera Movements] UI extension loaded.");
