create table Prov06_Taxonomies_IND diststyle key distkey(submitting_state_prov_id) compound sortkey (
    tms_run_id,
    submitting_state,
    submitting_state_prov_id
) as
select
    T.*,
    cast(F.label as smallint) as PRVDR_CLSFCTN_IND
from
    #Prov06_Taxonomies_ALL T left 
    join prv_formats_sm F on F.fmtname = 'TAXTYP'
    and (
        Trim(T.PRVDR_CLSFCTN_CD) >= F.start
        and Trim(T.PRVDR_CLSFCTN_CD) <= F.
    end
)
order by
    T.tms_run_id,
    T.submitting_state,
    T.submitting_state_prov_id;

;