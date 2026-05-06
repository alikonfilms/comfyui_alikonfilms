/**
 * Clip Text Encode - Camera Movements
 * Web UI Extension for ComfyUI
 *
 * Snaps the concatenate slider to 0, 0.5, or 1.
 * Snaps the row_mix slider to 0 or 1.
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
                // ── Force-snap helper: replace widget value with getter/setter ──
                const forceSnapWidget = (widget, snapFn) => {
                    if (!widget) return;
                    let internalValue = snapFn(widget.value);

                    Object.defineProperty(widget, "value", {
                        get() { return internalValue; },
                        set(v) {
                            internalValue = snapFn(v);
                        },
                        configurable: true,
                    });
                };

                // ── Snap concatenate to 0, 0.5, or 1 ──────────────────────
                const concatWidget = this.widgets.find(w => w.name === "concatenate");
                forceSnapWidget(concatWidget, (val) => {
                    if (val <= 0.25) return 0.0;
                    if (val >= 0.75) return 1.0;
                    return 0.5;
                });

                // ── Snap "Choose Camera" to 0 or 1 ────────────────────────
                const rowMixWidget = this.widgets.find(w => w.name === "Choose Camera");
                forceSnapWidget(rowMixWidget, (val) => val < 0.5 ? 0.0 : 1.0);

                this.setSize(this.computeSize());
            }, 50);

            return result;
        };
    },
});

console.log("[Clip Text Encode - Camera Movements] UI extension loaded.");
