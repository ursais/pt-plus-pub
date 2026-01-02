import logging

from openupgradelib import openupgrade

_logger = logging.getLogger(__name__)


@openupgrade.migrate()
def migrate(env, version):

    # Drop the temporary column
    try:
        env.cr.execute(
            """
            ALTER TABLE l10n_pt_company_eac
            DROP COLUMN code_tmp;
        """
        )
        _logger.info("Temporary column code_tmp dropped.")

    except Exception as e:
        _logger.warning(
            f"(3) Could not drop 'code_tmp' column. "
            f"It may not exist or another error occurred: {e}"
        )
    _logger.info("Adding temporary column 'code_tmp' to table 'l10n_pt_company_eac'...")
    env.cr.execute(
        """
        ALTER TABLE l10n_pt_company_eac
            ADD COLUMN code_tmp varchar;
        """
    )
    _logger.info("Temporary column added.")

    # Set code_tmp to the same value as code
    _logger.info("Copying values from 'code' to 'code_tmp'...")
    env.cr.execute(
        """
        UPDATE l10n_pt_company_eac
        SET code_tmp = code;
        """
    )
    _logger.info("Values copied.")
