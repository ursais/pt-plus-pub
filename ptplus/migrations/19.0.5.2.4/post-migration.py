import logging

from openupgradelib import openupgrade

_logger = logging.getLogger(__name__)  # pylint: disable=C0103


@openupgrade.migrate()
def migrate(env, version):
    # These two views are found archived on upgraded databases. The module
    # data load updates their arch but never resets the active flag, so
    # reactivate them explicitly after the upgrade.
    _logger.info("Reactivating ptplus product views archived during upgrade")
    env.cr.execute(
        """
        UPDATE ir_ui_view v
        SET active = true
        FROM ir_model_data md
        WHERE md.model = 'ir.ui.view'
          AND md.res_id = v.id
          AND md.module = 'ptplus'
          AND md.name IN (
              'product_template_form_view_pt',
              'view_category_property_form_pt'
          )
        """
    )
