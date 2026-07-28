===================
Portugal - E-Fatura
===================

Synchronize supplier invoices the Tax Authority website or from an
E-Fatura .csv file:

* For every line in the e-fatura file, a new draft vendor bill or refund will
  be created if there isn't one already inserted with the same vendor and
  vendor reference.
* The vendor itself will also be created if necessary.
* If an e-fatura document already exists in the database, a warning will be
  displayed if its values don't match the e-fatura values.
* The relevant invoice data is saved in a custom table containing all the
  imported e-fatura lines so that the user can check at any time if the
  vendor invoices match their e-fatura data.

**Table of contents**

.. contents::
   :local:

Installation
============

Install the module with required dependencies:

* pip install bs4, requests_html
* add the module to an addons folder, restart Odoo, update the addons list and activate
  it.

Configuration
=============

This module adds a new section named 'E-Fatura (Import)' on the Invoicing tab
of the supplier form. In there you can fill the E-Fatura Product and E-Fatura
Tax fields. These values will become the default product and tax values for the
invoice lines created from the e-fatura files.

It's also recommended to create default values for these fields. This way the
invoices for all the new suppliers created from the e-fatura file will have an
invoice line with the default product and tax (otherwise the invoices will be
created without lines).

Usage
=====

Available soon.

Known issues / Roadmap
======================

Available soon.

Changelog
=========

5.9.0 (2026-07-28)
~~~~~~~~~~~~~~~~~~~

**Improvement**

- When an expense matches an e-fatura record whose vendor bill was already
  confirmed or belongs to another expense, posting the expense no longer
  blocks: a separate draft vendor bill is created (keeping the e-fatura
  reference and per-tax breakdown, but not the e-fatura link) and a note on
  the bill suggests merging the two bills with the Merge E-Fatura Invoices
  action.

5.7.0 (2026-07-24)
~~~~~~~~~~~~~~~~~~~

**Improvement**

- Expenses are now linked to their e-fatura record: the QR scan creates or
  identifies it right away, and posting the expense reuses the draft vendor
  bill already created by the e-fatura import (matching by document
  reference + vendor VAT in any format) instead of creating a duplicate.
- When the expense has an e-fatura record and no bill exists yet, the vendor
  bill is created with one line per e-fatura tax line, so multi-rate
  receipts (e.g. 6% + 23%) get the correct per-tax breakdown.
- Bills created from expenses carry the pure document reference, so a later
  e-fatura import links to them instead of creating a new invoice.
- The expense tax fields are hidden when the expense has an e-fatura record
  (Portuguese companies only): the real per-tax breakdown lives in the
  e-fatura record and the single-value expense tax is misleading.

5.6.0 (2026-07-24)
~~~~~~~~~~~~~~~~~~~

**Improvement**

- Automatically scan the receipt for a Portuguese QR code when it is attached
  to an existing draft expense, either through the "Attach Receipt" button or
  the chatter.

5.5.0 (2026-07-24)
~~~~~~~~~~~~~~~~~~~

**Improvement**

- Add a manual "Scan QR" button to the expense form (same behaviour as the
  vendor bill one), so receipts attached after the expense is created can
  also be scanned. The scan now looks at every attachment of the expense,
  not only the main one.

5.4.0 (2026-07-23)
~~~~~~~~~~~~~~~~~~~

**Improvement**

- Rework the QR code detection of vendor bill attachments: decode the images
  embedded in PDFs at native resolution before falling back to page renders,
  enhance low-quality scans (thermal receipts, photos), only pick the fiscal
  QR code when a document carries several, and switch the decoder from
  pyzbar/zbar to OpenCV WeChatQRCode (no OS-level dependency required).
- Scan the Portuguese QR code of expense receipts too (Expenses upload):
  fill the expense total amount, date, vendor and description from the QR
  code data. New dependency on ptplus_expense.
- The opencv-contrib-python-headless python package is an optional
  dependency: when it is not installed the QR code scan is skipped with a
  log warning, uploads and upgrades are never blocked.

5.1.0 (2023-11-16)
~~~~~~~~~~~~~~~~~~~

**Features**

- Initial changelog

Credits
=======

Authors
~~~~~~~

* Exo Software, Lda.

Contributors
~~~~~~~~~~~~

* `Exo Software <https://exosoftware.pt>`_:

  * Pedro Castro Silva
  * André Leite
  * João Costa

* `Growfactor <https://www.growfactor.pt>`_:

  * Álvaro Ribeiro
  * Luís Homem

Maintainers
~~~~~~~~~~~

This module is maintained by Exo Software, Lda.

.. image:: https://exosoftware.pt/logo.png
   :alt: Exo Software
   :target: https://exosoftware.pt
   :width: 100px
