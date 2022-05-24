create
or replace temporary view ELG00005 as
select
    a.TMSIS_RUN_ID,
    a.TMSIS_ACTV_IND,
    case
        when a.SUBMTG_STATE_CD = '96' then '19'
        when a.SUBMTG_STATE_CD = '97' then '42'
        when a.SUBMTG_STATE_CD = '93' then '56'
        when a.SUBMTG_STATE_CD = '94' then '30'
        else a.SUBMTG_STATE_CD
    end as SUBMTG_STATE_CD,
    a.REC_NUM,
    case
        when upper(trim(a.ELGBLTY_GRP_CD)) in(
            '01',
            '02',
            '03',
            '04',
            '05',
            '06',
            '07',
            '08',
            '09',
            '1',
            '2',
            '3',
            '4',
            '5',
            '6',
            '7',
            '8',
            '9',
            '11',
            '12',
            '13',
            '14',
            '15',
            '16',
            '17',
            '18',
            '19',
            '20',
            '21',
            '22',
            '23',
            '24',
            '25',
            '26',
            '27',
            '28',
            '29',
            '30',
            '31',
            '32',
            '33',
            '34',
            '35',
            '36',
            '37',
            '38',
            '39',
            '40',
            '41',
            '42',
            '43',
            '44',
            '45',
            '46',
            '47',
            '48',
            '49',
            '50',
            '51',
            '52',
            '53',
            '54',
            '55',
            '56',
            '59',
            '60',
            '61',
            '62',
            '63',
            '64',
            '65',
            '66',
            '67',
            '68',
            '69',
            '70',
            '71',
            '72',
            '73',
            '74',
            '75',
            '76'
        ) then upper(trim(a.ELGBLTY_GRP_CD))
        else null
    end as ELGBLTY_GRP_CD,
    case
        when upper(trim(a.DUAL_ELGBL_CD)) in(
            '00',
            '01',
            '02',
            '03',
            '04',
            '05',
            '06',
            '08',
            '09',
            '10',
            '0',
            '1',
            '2',
            '3',
            '4',
            '5',
            '6',
            '8',
            '9'
        ) then upper(trim(a.DUAL_ELGBL_CD))
        else null
    end as DUAL_ELGBL_CD,
    case
        when upper(trim(a.ELGBLTY_CHG_RSN_CD)) in(
            '01',
            '02',
            '03',
            '04',
            '05',
            '06',
            '07',
            '08',
            '09',
            '1',
            '2',
            '3',
            '4',
            '5',
            '6',
            '7',
            '8',
            '9',
            '11',
            '12',
            '13',
            '14',
            '15',
            '16',
            '17',
            '18',
            '19',
            '20',
            '21',
            '22'
        ) then upper(trim(a.ELGBLTY_CHG_RSN_CD))
        else null
    end as ELGBLTY_CHG_RSN_CD,
    a.MSIS_CASE_NUM,
    case
        when upper(trim(a.ELGBLTY_MDCD_BASIS_CD)) in(
            '00',
            '01',
            '02',
            '03',
            '04',
            '05',
            '06',
            '07',
            '08',
            '10',
            '11'
        ) then upper(trim(a.ELGBLTY_MDCD_BASIS_CD))
        else null
    end as ELGBLTY_MDCD_BASIS_CD,
    case
        when upper(trim(a.CARE_LVL_STUS_CD)) in(
            '001',
            '002',
            '003',
            '004',
            '005',
            '01',
            '02',
            '03',
            '04',
            '05',
            '1',
            '2',
            '3',
            '4',
            '5'
        ) then upper(trim(a.CARE_LVL_STUS_CD))
        else null
    end as CARE_LVL_STUS_CD,
    case
        when upper(trim(a.SSDI_IND)) in('0', '1') then upper(trim(a.SSDI_IND))
        else null
    end as SSDI_IND,
    case
        when upper(trim(a.SSI_IND)) in('0', '1') then upper(trim(a.SSI_IND))
        else null
    end as SSI_IND,
    case
        when upper(trim(a.SSI_STATE_SPLMT_STUS_CD)) in('000', '001', '002') then upper(trim(a.SSI_STATE_SPLMT_STUS_CD))
        else null
    end as SSI_STATE_SPLMT_STUS_CD,
    case
        when upper(trim(a.SSI_STUS_CD)) in('000', '001', '002') then upper(trim(a.SSI_STUS_CD))
        else null
    end as SSI_STUS_CD,
    a.STATE_SPEC_ELGBLTY_FCTR_TXT,
    case
        when upper(trim(a.BIRTH_CNCPTN_IND)) in('0', '1') then upper(trim(a.BIRTH_CNCPTN_IND))
        else null
    end as BIRTH_CNCPTN_IND,
    case
        when upper(trim(a.MAS_CD)) in('0', '1', '2', '3', '4', '5') then upper(trim(a.MAS_CD))
        else null
    end as MAS_CD,
    case
        when upper(trim(a.RSTRCTD_BNFTS_CD)) in(
            '0',
            '1',
            '2',
            '3',
            '4',
            '5',
            '6',
            '7',
            'A',
            'B',
            'C',
            'D',
            'E',
            'F'
        ) then upper(trim(a.RSTRCTD_BNFTS_CD))
        else null
    end as RSTRCTD_BNFTS_CD,
    case
        when upper(trim(a.TANF_CASH_CD)) in('0', '1', '2') then upper(trim(a.TANF_CASH_CD))
        else null
    end as TANF_CASH_CD,
    a.ELGBLTY_DTRMNT_EFCTV_DT,
    a.ELGBLTY_DTRMNT_END_DT,
    case
        when upper(trim(a.PRMRY_ELGBLTY_GRP_IND)) in('0', '1') then upper(trim(a.PRMRY_ELGBLTY_GRP_IND))
        else null
    end as PRMRY_ELGBLTY_GRP_IND,
    upper(a.MSIS_IDENT_NUM) as MSIS_IDENT_NUM,
    a.TMSIS_RPTG_PRD
from
    tmsis.TMSIS_ELGBLTY_DTRMNT as a -- left join data_anltcs_dm_prod.state_submsn_type s on a.submtg_state_cd = s.submtg_state_cd and upper(s.fil_type) = 'ELG'
where
    (
        a.TMSIS_ACTV_IND = 1
        and (
            ELGBLTY_DTRMNT_EFCTV_DT <= to_date('2021-11-30')
            and (
                ELGBLTY_DTRMNT_END_DT >= to_date('2021-11-01')
                or ELGBLTY_DTRMNT_END_DT is NULL
            )
        )
    ) -- and (
    --     (
    --         upper(coalesce(s.submsn_type, 'X')) <> 'CSO'
    --         and a.TMSIS_RPTG_PRD >= to_date('2021-11-01')
    --     )
    --     or (upper(coalesce(s.submsn_type, 'X')) = 'CSO')
    -- )
    and concat(a.submtg_state_cd, a.tmsis_run_id) in (
        concat('01', 4574),
        concat('02', 4567),
        concat('04', 4554),
        concat('05', 4550),
        concat('06', 4556),
        concat('08', 4578),
        concat('09', 4568),
        concat('10', 4557),
        concat('11', 4545),
        concat('12', 4555),
        concat('13', 4538),
        concat('15', 4558),
        concat('16', 4579),
        concat('17', 4584),
        concat('18', 4561),
        concat('19', 4548),
        concat('20', 4589),
        concat('21', 4553),
        concat('22', 4573),
        concat('23', 4540),
        concat('24', 4569),
        concat('25', 4559),
        concat('26', 4585),
        concat('27', 4539),
        concat('28', 4594),
        concat('29', 4562),
        concat('30', 4580),
        concat('31', 4546),
        concat('32', 4551),
        concat('33', 4570),
        concat('34', 4590),
        concat('35', 4552),
        concat('36', 4566),
        concat('37', 4517),
        concat('38', 4575),
        concat('39', 4571),
        concat('40', 4593),
        concat('41', 4541),
        concat('42', 4560),
        concat('44', 4592),
        concat('45', 4544),
        concat('46', 4549),
        concat('47', 4583),
        concat('48', 4507),
        concat('49', 4577),
        concat('50', 4581),
        concat('51', 4564),
        concat('53', 4587),
        concat('54', 4582),
        concat('55', 4565),
        concat('56', 4423),
        concat('72', 4547),
        concat('78', 4563),
        concat('93', 4447),
        concat('97', 4543)
    )
    and a.msis_ident_num is not null
limit
    1000