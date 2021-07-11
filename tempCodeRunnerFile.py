def generate_ui():
    ui_manager.clear_and_reset()
    lm = 30     # Left margin

    generate_button = pgui.elements.UIButton(relative_rect=pg.Rect(lm, 125, 200, 50),
                                            text="Generate", manager=ui_manager,
                                            object_id="generate_button")
