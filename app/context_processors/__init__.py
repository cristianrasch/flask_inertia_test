def register_ctx_processors(app):
    from .assets import asset_processors

    app.context_processor(asset_processors)
