# Create a tax ID

Creates a new account or customer `tax_id` object.

## Returns

The created `tax_id` object.

## Parameters

- `type` (string, required)
  Type of the tax ID, one of `ad_nrt`, `ae_trn`, `al_tin`, `am_tin`, `ao_tin`, `ar_cuit`, `au_abn`, `au_arn`, `aw_tin`, `az_tin`, `ba_tin`, `bb_tin`, `bd_bin`, `bf_ifu`, `bg_uic`, `bh_vat`, `bj_ifu`, `bo_tin`, `br_cnpj`, `br_cpf`, `bs_tin`, `by_tin`, `ca_bn`, `ca_gst_hst`, `ca_pst_bc`, `ca_pst_mb`, `ca_pst_sk`, `ca_qst`, `cd_nif`, `ch_uid`, `ch_vat`, `cl_tin`, `cm_niu`, `cn_tin`, `co_nit`, `cr_tin`, `cv_nif`, `de_stn`, `do_rcn`, `ec_ruc`, `eg_tin`, `es_cif`, `et_tin`, `eu_oss_vat`, `eu_vat`, `gb_vat`, `ge_vat`, `gn_nif`, `hk_br`, `hr_oib`, `hu_tin`, `id_npwp`, `il_vat`, `in_gst`, `is_vat`, `jp_cn`, `jp_rn`, `jp_trn`, `ke_pin`, `kg_tin`, `kh_tin`, `kr_brn`, `kz_bin`, `la_tin`, `li_uid`, `li_vat`, `lk_vat`, `ma_vat`, `md_vat`, `me_pib`, `mk_vat`, `mr_nif`, `mx_rfc`, `my_frp`, `my_itn`, `my_sst`, `ng_tin`, `no_vat`, `no_voec`, `np_pan`, `nz_gst`, `om_vat`, `pe_ruc`, `ph_tin`, `pl_nip`, `ro_tin`, `rs_pib`, `ru_inn`, `ru_kpp`, `sa_vat`, `sg_gst`, `sg_uen`, `si_tin`, `sn_ninea`, `sr_fin`, `sv_nit`, `th_vat`, `tj_tin`, `tr_tin`, `tw_vat`, `tz_vat`, `ua_vat`, `ug_tin`, `us_ein`, `uy_ruc`, `uz_tin`, `uz_vat`, `ve_rif`, `vn_tin`, `za_vat`, `zm_tin`, or `zw_tin`

- `value` (string, required)
  Value of the tax ID.

- `owner` (object, optional)
  The account or customer the tax ID belongs to. Defaults to `owner[type]=self`.

  - `owner.type` (enum, required)
    Type of owner referenced.
Possible enum values:
    - `account`
      Indicates an account is being referenced.

    - `application`
      Indicates an application is being referenced.

    - `customer`
      Indicates a customer is being referenced.

    - `self`
      Indicates that the account being referenced is the account making the API request.

  - `owner.account` (string, optional)
    Connected Account the tax ID belongs to. Required when `type=account`

  - `owner.customer` (string, optional)
    Customer the tax ID belongs to. Required when `type=customer`

  - `owner.customer_account` (string, optional)
    ID of the Account representing the customer that the tax ID belongs to. Can be used in place of `customer` when `type=customer`

```curl
curl https://api.stripe.com/v1/tax_ids \
  -u "<<YOUR_SECRET_KEY>>" \
  -d type=eu_vat \
  -d value=DE123456789
```

### Response

```json
{
  "id": "txi_1NuMB12eZvKYlo2CMecoWkZd",
  "object": "tax_id",
  "country": "DE",
  "created": 123456789,
  "customer": null,
  "livemode": false,
  "type": "eu_vat",
  "value": "DE123456789",
  "verification": null,
  "owner": {
    "type": "self",
    "customer": null
  }
}
```
