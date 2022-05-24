create temp table ELG00006_recCt distkey(msis_ident_num) sortkey(submtg_state_cd, msis_ident_num, recCt) as
select
    submtg_state_cd,
    msis_ident_num,
    count(TMSIS_RUN_ID) as recCt
from
    ELG00006
group by
    submtg_state_cd,
    msis_ident_num