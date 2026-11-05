import logging

from openupgradelib import openupgrade

_logger = logging.getLogger(__name__)  # pylint: disable=C0103


@openupgrade.migrate()
def migrate(env, version):
    # Databases carried over from older versions may have UI-customized views
    # (no xmlid) on product.product embedding template form content with
    # l10n_pt_legal_categ. When the field is gone, the view fails custom view
    # validation, so deactivate it.
    if "l10n_pt_legal_categ" in env["product.product"]._fields:
        return
    views = env["ir.ui.view"].search(
        [("model", "=", "product.product"), ("arch_db", "ilike", "l10n_pt_legal_categ")]
    )
    owned_ids = (
        env["ir.model.data"]
        .search([("model", "=", "ir.ui.view"), ("res_id", "in", views.ids)])
        .mapped("res_id")
    )
    stale = views - env["ir.ui.view"].browse(owned_ids)
    if stale:
        _logger.info("Deactivating stale custom views: %s", stale.ids)
        stale.write({"active": False})
