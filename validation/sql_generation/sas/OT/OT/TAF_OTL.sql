INSERT INTO
    data_anltcs_dm_prod.TAF_OTL (
        DA_RUN_ID,
        OT_LINK_KEY,
        OT_VRSN,
        OT_FIL_DT,
        TMSIS_RUN_ID,
        MSIS_IDENT_NUM,
        SUBMTG_STATE_CD,
        ORGNL_CLM_NUM,
        ADJSTMT_CLM_NUM,
        ORGNL_LINE_NUM,
        ADJSTMT_LINE_NUM,
        ADJDCTN_DT,
        LINE_ADJSTMT_IND,
        ADJSTMT_LINE_RSN_CD,
        CLL_STUS_CD,
        SRVC_BGNNG_DT,
        SRVC_ENDG_DT,
        REV_CD,
        PRCDR_CD,
        PRCDR_CD_DT,
        PRCDR_CD_IND,
        PRCDR_1_MDFR_CD,
        IMNZTN_TYPE_CD,
        BILL_AMT,
        ALOWD_AMT,
        COPAY_AMT,
        TPL_AMT,
        MDCD_PD_AMT,
        MDCD_FFS_EQUIV_AMT,
        MDCR_PD_AMT,
        OTHR_INSRNC_AMT,
        ACTL_SRVC_QTY,
        ALOWD_SRVC_QTY,
        TOS_CD,
        BNFT_TYPE_CD,
        HCBS_SRVC_CD,
        HCBS_TXNMY,
        SRVCNG_PRVDR_NUM,
        SRVCNG_PRVDR_NPI_NUM,
        SRVCNG_PRVDR_TXNMY_CD,
        SRVCNG_PRVDR_TYPE_CD,
        SRVCNG_PRVDR_SPCLTY_CD,
        TOOTH_DSGNTN_SYS_CD,
        TOOTH_NUM,
        TOOTH_ORAL_CVTY_AREA_DSGNTD_CD,
        TOOTH_SRFC_CD,
        CMS_64_FED_REIMBRSMT_CTGRY_CD,
        XIX_SRVC_CTGRY_CD,
        XXI_SRVC_CTGRY_CD,
        STATE_NOTN_TXT,
        NDC_CD,
        PRCDR_2_MDFR_CD,
        PRCDR_3_MDFR_CD,
        PRCDR_4_MDFR_CD,
        HCPCS_RATE,
        SELF_DRCTN_TYPE_CD,
        PRE_AUTHRZTN_NUM,
        UOM_CD,
        NDC_QTY,
        LINE_NUM,
        PRCDR_CCS_CTGRY_CD,
        SRVCNG_PRVDR_NPPES_TXNMY_CD
    )
SELECT
    *
FROM
    OTL