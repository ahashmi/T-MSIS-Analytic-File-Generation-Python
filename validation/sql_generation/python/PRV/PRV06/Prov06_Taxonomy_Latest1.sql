create
or replace temporary view Prov06_Taxonomy_Latest1 as
select
    T.*,
    R.SPCL
from
    Prov_Taxonomy_Classification T
    inner join Prov02_Main R on T.tms_run_id = R.tms_run_id
    and T.submitting_state = R.submitting_state
    and upper(T.submitting_state_prov_id) = R.submitting_state_prov_id
order by
    T.tms_run_id,
    T.submitting_state,
    T.submitting_state_prov_id