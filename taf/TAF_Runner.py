import logging

from datetime import datetime


# -------------------------------------------------------------------------------------
#
#
#
#
# -------------------------------------------------------------------------------------
class TAF_Runner():

    PERFORMANCE = 11

    # ---------------------------------------------------------------------------------
    #
    #   reporting_period = SUBSTR(JOB_PARMS_TXT,1,10) AS RPTPD FORMAT=$10.
    #   e.g. '2020-01-31'
    #
    #
    # ---------------------------------------------------------------------------------
    def __init__(self, reporting_period: str, state_code: str, run_id: str):

        from datetime import date, datetime, timedelta

        self.now = datetime.now()
        self.version = '0A'

        self.initialize_logger(self.now)

        # FIXME: this should be monotonic or something more crafty
        self.DA_RUN_ID = datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')
        self.DA_SCHEMA = 'taf_python'

        self.reporting_period = datetime.strptime(reporting_period, '%Y-%m-%d')

        begmon = self.reporting_period
        begmon = date(begmon.year, begmon.month, 1)
        self.begmon = begmon.strftime('%Y-%m-%d').upper()
        self.st_dt = f'{self.begmon}'

        self.BSF_FILE_DATE = int(self.reporting_period.strftime('%Y%m'))
        self.TAF_FILE_DATE = self.BSF_FILE_DATE

        self.RPT_PRD = f'{self.reporting_period.strftime("%Y-%m-%d")}'
        self.RPT_OUT = f"{self.reporting_period.strftime('%d%b%Y').upper()}"

        if self.now.month == 12:  # December
            last_day = date(self.now.year, self.now.month, 31)
        else:
            last_day = date(self.now.year, self.now.month + 1, 1) - timedelta(days=1)

        self.FILE_DT_END = last_day.strftime('%Y-%m-%d').upper()

        if len(state_code) and len(run_id):
            if (state_code.find(',') != -1) and (run_id.find(',') != -1):
                self.combined_list = list(tuple(zip(eval(state_code), eval(run_id))))
            else:
                self.combined_list = [(eval(state_code), eval(run_id)),]
        else:
            self.combined_list = []

        self.sql = {}
        self.plan = {}

    # --------------------------------------------------------------------
    #
    #
    #
    # --------------------------------------------------------------------
    def print(self):
        print('Version:\t' + self.version)
        print('-----------------------------------------------------')
        print('')
        print('-----------------------------------------------------')
        print('begmon:\t' + str(self.begmon))
        print('st_dt:\t' + self.st_dt)
        print('BSF_FILE_DATE:\t' + str(self.BSF_FILE_DATE))
        print('TAF_FILE_DATE:\t' + str(self.TAF_FILE_DATE))
        print('RPT_PRD:\t' + str(self.RPT_PRD))
        print('FILE_DT_END:\t' + str(self.FILE_DT_END))
        print('DA_SCHEMA:\t' + str(self.DA_SCHEMA))
        print('COMBINED_LIST:\t' + str(self.combined_list))

    # -----------------------------------------------------------------------------
    #
    #
    #
    # -----------------------------------------------------------------------------
    def get_link_key(self):

        return f"""
            cast ((concat('{self.version }',  '-',  {self.TAF_FILE_DATE},  '-',  NEW_SUBMTG_STATE_CD,  '-',
              trim(COALESCE(NULLIF(ORGNL_CLM_NUM,'~'),'0')), '-',  trim(COALESCE(NULLIF(ADJSTMT_CLM_NUM,'~'),'0')),  '-',
                CAST(year(ADJDCTN_DT) AS CHAR(4)), CAST(DATE_PART('MONTH',ADJDCTN_DT) AS CHAR(2)),
                 CAST(DATE_PART('DAY',ADJDCTN_DT) AS CHAR(2)), '-',  COALESCE(ADJSTMT_IND_CLEAN,'X'))) as varchar(126))
        """

    # -----------------------------------------------------------------------------
    #
    #
    #
    # -----------------------------------------------------------------------------
    def get_link_key_line(self):

        return f"""
            cast ((concat('{self.version }',  '-',  {self.TAF_FILE_DATE},  '-',  NEW_SUBMTG_STATE_CD_LINE,  '-',
              trim(COALESCE(NULLIF(ORGNL_CLM_NUM_LINE,'~'),'0')), '-',  trim(COALESCE(NULLIF(ADJSTMT_CLM_NUM_LINE,'~'),'0')),  '-',
                CAST(year(ADJDCTN_DT_LINE) AS CHAR(4)), CAST(DATE_PART('MONTH',ADJDCTN_DT_LINE) AS CHAR(2)),
                 CAST(DATE_PART('DAY',ADJDCTN_DT_LINE) AS CHAR(2)), '-',  COALESCE(LINE_ADJSTMT_IND_CLEAN,'X'))) as varchar(126))
        """

    # --------------------------------------------------------------------
    #
    #
    #
    # --------------------------------------------------------------------
    @staticmethod
    def compress(string):
        return ' '.join(string.split())

    # --------------------------------------------------------------------
    #
    #
    #
    # --------------------------------------------------------------------
    def log(self, viewname: str, sql=''):
        self.logger.info('\t' + viewname)
        if sql != '':
            self.logger.debug(TAF_Runner.compress(sql.replace('\n', '')))

    # --------------------------------------------------------------------
    #
    #
    #
    # --------------------------------------------------------------------
    def initialize_logger(self, now: datetime):

        # data_anltcs_dm_prod.state_submsn_type
        # SELECT * FROM data_anltcs_dm_prod.PGM_AUDT_CNT_LKP WHERE PGM_NAME = '002_bsf_ELG00002' and step_name = '0.1. create_initial_table' ;
        # insert into data_anltcs_dm_prod.PGM_AUDT_CNTS select da_run_id, pgm_audt_cnt_id, nullif(submtg_state_cd, 'xx'),audt_cnt_val from row_count1 order by audt_cnt_val desc limit 48
        # SELECT * FROM data_anltcs_dm_prod.PGM_AUDT_CNT_LKP WHERE PGM_NAME = '002_bsf_ELG00002' and step_name = '0.2. MultiIds' ;

        # left join data_anltcs_dm_prod.state_submsn_typeSELECT * FROM data_anltcs_dm_prod.PGM_AUDT_CNT_LKP WHERE PGM_NAME = '003_bsf_ELG00003' and step_name = '0.1. create_initial_table' ;

        # left join data_anltcs_dm_prod.state_submsn_type s on a.submtg_state_cd = s.submtg_state_cd and upper(s.fil_type) = 'ELG'

        # SELECT * FROM data_anltcs_dm_prod.PGM_AUDT_CNT_LKP WHERE PGM_NAME = '003_bsf_ELG00003' and step_name = '0.1. create_initial_table' ;
        # insert into data_anltcs_dm_prod.PGM_AUDT_CNTS
        # insert into data_anltcs_dm_prod.PGM_AUDT_CNTS
        # insert into data_anltcs_dm_prod.PGM_AUDT_CNTS
        # SELECT * FROM data_anltcs_dm_prod.PGM_AUDT_CNT_LKP WHERE PGM_NAME = '004_bsf_ELG00004' and step_name = '0.1. create_initial_table' ;
        # insert into data_anltcs_dm_prod.PGM_AUDT_CNTS
        # insert into data_anltcs_dm_prod.PGM_AUDT_CNTS
        # insert into data_anltcs_dm_prod.PGM_AUDT_CNTS
        # SELECT * FROM data_anltcs_dm_prod.PGM_AUDT_CNT_LKP WHERE PGM_NAME = '005_bsf_ELG00005' and step_name = '0.1. create_initial_table' ;
        # insert into data_anltcs_dm_prod.PGM_AUDT_CNTS
        # insert into data_anltcs_dm_prod.PGM_AUDT_CNTS
        # insert into data_anltcs_dm_prod.PGM_AUDT_CNTS
        # SELECT * FROM data_anltcs_dm_prod.PGM_AUDT_CNT_LKP WHERE PGM_NAME = '005_bsf_ELG00005' and step_name = '0.2. MultiIds' ;

        # SELECT * FROM data_anltcs_dm_prod.PGM_AUDT_CNT_LKP WHERE PGM_NAME = '021_bsf_ELG00021' and step_name = '21.3 join' ;

        logging.addLevelName(TAF_Runner.PERFORMANCE, 'PERFORMANCE')

        self.logger = logging.getLogger('dqm_log')
        self.logger.setLevel(logging.INFO)

        ch = logging.StreamHandler()

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)

        if (self.logger.hasHandlers()):
            self.logger.handlers.clear()

        self.logger.addHandler(ch)

    # --------------------------------------------------------------------
    #
    #
    #
    # --------------------------------------------------------------------
    def fetch_combined_list(self):

        from pyspark.sql import SparkSession
        spark = SparkSession.getActiveSession()

        # TODO: this is supposed to be queried from cms_prod.tmsis_fhdr_rec_elgblty

        sdf = spark.sql("""
            select distinct
                submtg_state_cd,
                max(tmsis_run_id) as tmsis_run_id
            from
                tmsis.tmsis_fhdr_rec_elgblty
            where tmsis_actv_ind = 1 and
                tmsis_rptg_prd is not null and
                tot_rec_cnt > 0 and
                ssn_ind in ('1','0')
            group by
                submtg_state_cd
            order by
                submtg_state_cd""")

        rdd = sdf.rdd
        self.combined_list = rdd.map(tuple)
        # for j in self.combined_list.collect():
        #     print(j)

    # ---------------------------------------------------------------------------------
    #
    #
    #
    #
    # ---------------------------------------------------------------------------------
    def get_combined_list(self):
        tuples = []
        for j in self.combined_list:
            tuples.append('concat' + str(j))
        return ','.join(tuples)

    # ---------------------------------------------------------------------------------
    #
    #
    #
    #
    # ---------------------------------------------------------------------------------
    @staticmethod
    def ssn_ind():

        return """
                create or replace temporary view ssn_ind as
                select distinct submtg_state_cd
                    ,max(ssn_ind) as ssn_ind
                    ,max(tmsis_run_id) as tmsis_run_id
                from tmsis.tmsis_fhdr_rec_elgblty
                where tmsis_actv_ind = 1
                    and tmsis_rptg_prd is not null
                    and tot_rec_cnt > 0
                    and ssn_ind IN ('1','0')
                group by submtg_state_cd
        """

    # ---------------------------------------------------------------------------------
    #
    #
    #
    #
    # ---------------------------------------------------------------------------------
    def append(self, segment: str, z: str):

        if segment not in self.plan.keys():
            self.plan[segment] = []

        v = '\n'.join(z.split('\n')[0:2])
        vs = v.split()

        if len(vs) >= 5:
            self.sql[vs[5]] = z

        # self.log(f"{self.tab_no}", z)
        self.plan[segment].append(z)

    # ---------------------------------------------------------------------------------
    #
    #
    #
    #
    # ---------------------------------------------------------------------------------
    def view_plan(self):

        for segment, chain in self.plan.items():
            for sql in chain:
                print(f"-- {segment}")
                print(sql)

    # ---------------------------------------------------------------------------------
    #
    #
    #
    #
    # ---------------------------------------------------------------------------------
    def write(self, module: str = ''):

        print('Writing SQL Files ...')

        for segment, chain in self.plan.items():

            print('\t' + segment + '...')
            for z in chain:

                v = '\n'.join(z.split('\n')[0:2])
                vs = v.split()

                if len(vs) >= 5:
                    # fn = './test/sql/python/' + segment + '/' + vs[5] + '.sql'
                    if module != '':
                        fn = '../../sql/python/' + module + '/' + segment + '/' + vs[5] + '.sql'
                    else:
                        fn = '../../sql/python/' + segment + '/' + vs[5] + '.sql'
                    print(fn)
                    f = open(fn, 'w')
                    f.write(z)
                    f.close()

    # ---------------------------------------------------------------------------------
    #
    #
    #
    #
    # ---------------------------------------------------------------------------------
    def run(self):

        from taf.BSF.BSF_Metadata import BSF_Metadata
        from pyspark.sql.types import StructType, StructField, StringType
        import pandas as pd

        from pyspark.sql import SparkSession
        spark = SparkSession.getActiveSession()

        df = pd.DataFrame(BSF_Metadata.prmry_lang_cd, columns=['LANG_CD'])
        schema = StructType([StructField("LANG_CD", StringType(), True)])

        self.logger.info('Creating Primary Language Code Table...')

        sdf = spark.createDataFrame(data=df, schema=schema)
        sdf.registerTempTable('prmry_lang_cd')

        self.logger.info('Creating SSN Indicator View...')

        spark.sql(self.ssn_ind())

        self.logger.info('Creating TAF Views...')

        for segment, chain in self.plan.items():
            self.logger.info('\t' + segment + '...')
            for z in chain:
                # self.logger.info('\n'.join(z.split('\n')[0:2]))

                v = '\n'.join(z.split('\n')[0:2])
                vs = v.split()

                if len(vs) >= 5:
                    print('\t\t' + vs[5])

                # self.logger.info('\t\t' + v.split()[5])

                spark.sql(z)

    # ---------------------------------------------------------------------------------
    #
    #
    #
    #
    # ---------------------------------------------------------------------------------
    def audit(self):

        from taf.BSF.BSF_Metadata import BSF_Metadata
        from pyspark.sql.types import StructType, StructField, StringType
        import pandas as pd

        from pyspark.sql import SparkSession
        spark = SparkSession.getActiveSession()

        if spark:

            df = pd.DataFrame(BSF_Metadata.prmry_lang_cd, columns=['LANG_CD'])
            schema = StructType([StructField("LANG_CD", StringType(), True)])

            sdf = spark.createDataFrame(data=df, schema=schema)
            sdf.registerTempTable('prmry_lang_cd')

            self.logger.info('Auditing  "0.1. create_initial_table" - "distinct msis_ident_num" ...')

            pdf = None
            for segment, chain in self.plan.items():
                self.logger.info('\t' + segment + '...')
                for z in chain:
                    v = '\n'.join(z.split('\n')[0:2])
                    vs = v.split()

                    if len(vs) >= 5:
                        # print('\t\t' + vs[5])

                        obj_name = v.split()[5]
                        if obj_name in ['ELG00002', 'ELG00003', 'ELG00004', 'ELG00005', 'ELG00006', 'ELG00007', 'ELG00008', 'ELG00009', 'ELG00010',
                                        'ELG00011', 'ELG00012', 'ELG00013', 'ELG00014', 'ELG00015', 'ELG00016', 'ELG00017', 'ELG00018', 'ELG00020',
                                        'ELG00021', 'TPL00002']:
                            sdf_audit_cnt = spark.sql(f"""
                                select
                                    '{obj_name}' as obj_name,
                                    submtg_state_cd,
                                    count(distinct msis_ident_num) as audt_cnt_val
                                from
                                    {obj_name}
                                group by
                                    obj_name,
                                    submtg_state_cd
                                order by
                                    obj_name,
                                    submtg_state_cd""")

                            if pdf is None:
                                print(obj_name)
                                pdf = sdf_audit_cnt.toPandas()
                            else:
                                print("appending - " + obj_name)
                                pdf = pdf.append(sdf_audit_cnt.toPandas())

            return pdf
        else:
            self.logger.info('No valid Spark Session')
            return None


# -----------------------------------------------------------------------------
# CC0 1.0 Universal

# Statement of Purpose

# The laws of most jurisdictions throughout the world automatically confer
# exclusive Copyright and Related Rights (defined below) upon the creator and
# subsequent owner(s) (each and all, an "owner") of an original work of
# authorship and/or a database (each, a "Work").

# Certain owners wish to permanently relinquish those rights to a Work for the
# purpose of contributing to a commons of creative, cultural and scientific
# works ("Commons") that the public can reliably and without fear of later
# claims of infringement build upon, modify, incorporate in other works, reuse
# and redistribute as freely as possible in any form whatsoever and for any
# purposes, including without limitation commercial purposes. These owners may
# contribute to the Commons to promote the ideal of a free culture and the
# further production of creative, cultural and scientific works, or to gain
# reputation or greater distribution for their Work in part through the use and
# efforts of others.

# For these and/or other purposes and motivations, and without any expectation
# of additional consideration or compensation, the person associating CC0 with a
# Work (the "Affirmer"), to the extent that he or she is an owner of Copyright
# and Related Rights in the Work, voluntarily elects to apply CC0 to the Work
# and publicly distribute the Work under its terms, with knowledge of his or her
# Copyright and Related Rights in the Work and the meaning and intended legal
# effect of CC0 on those rights.

# 1. Copyright and Related Rights. A Work made available under CC0 may be
# protected by copyright and related or neighboring rights ("Copyright and
# Related Rights"). Copyright and Related Rights include, but are not limited
# to, the following:

#   i. the right to reproduce, adapt, distribute, perform, display, communicate,
#   and translate a Work

#   ii. moral rights retained by the original author(s) and/or performer(s)

#   iii. publicity and privacy rights pertaining to a person's image or likeness
#   depicted in a Work

#   iv. rights protecting against unfair competition in regards to a Work,
#   subject to the limitations in paragraph 4(a), below

#   v. rights protecting the extraction, dissemination, use and reuse of data in
#   a Work

#   vi. database rights (such as those arising under Directive 96/9/EC of the
#   European Parliament and of the Council of 11 March 1996 on the legal
#   protection of databases, and under any national implementation thereof,
#   including any amended or successor version of such directive) and

#   vii. other similar, equivalent or corresponding rights throughout the world
#   based on applicable law or treaty, and any national implementations thereof.

# 2. Waiver. To the greatest extent permitted by, but not in contravention of,
# applicable law, Affirmer hereby overtly, fully, permanently, irrevocably and
# unconditionally waives, abandons, and surrenders all of Affirmer's Copyright
# and Related Rights and associated claims and causes of action, whether now
# known or unknown (including existing as well as future claims and causes of
# action), in the Work (i) in all territories worldwide, (ii) for the maximum
# duration provided by applicable law or treaty (including future time
# extensions), (iii) in any current or future medium and for any number of
# copies, and (iv) for any purpose whatsoever, including without limitation
# commercial, advertising or promotional purposes (the "Waiver"). Affirmer makes
# the Waiver for the benefit of each member of the public at large and to the
# detriment of Affirmer's heirs and successors, fully intending that such Waiver
# shall not be subject to revocation, rescission, cancellation, termination, or
# any other legal or equitable action to disrupt the quiet enjoyment of the Work
# by the public as contemplated by Affirmer's express Statement of Purpose.

# 3. Public License Fallback. Should any part of the Waiver for any reason be
# judged legally invalid or ineffective under applicable law, then the Waiver
# shall be preserved to the maximum extent permitted taking into account
# Affirmer's express Statement of Purpose. In addition, to the extent the Waiver
# is so judged Affirmer hereby grants to each affected person a royalty-free,
# non transferable, non sublicensable, non exclusive, irrevocable and
# unconditional license to exercise Affirmer's Copyright and Related Rights in
# the Work (i) in all territories worldwide, (ii) for the maximum duration
# provided by applicable law or treaty (including future time extensions), (iii)
# in any current or future medium and for any number of copies, and (iv) for any
# purpose whatsoever, including without limitation commercial, advertising or
# promotional purposes (the "License"). The License shall be deemed effective as
# of the date CC0 was applied by Affirmer to the Work. Should any part of the
# License for any reason be judged legally invalid or ineffective under
# applicable law, such partial invalidity or ineffectiveness shall not
# invalidate the remainder of the License, and in such case Affirmer hereby
# affirms that he or she will not (i) exercise any of his or her remaining
# Copyright and Related Rights in the Work or (ii) assert any associated claims
# and causes of action with respect to the Work, in either case contrary to
# Affirmer's express Statement of Purpose.

# 4. Limitations and Disclaimers.

#   a. No trademark or patent rights held by Affirmer are waived, abandoned,
#   surrendered, licensed or otherwise affected by this document.

#   b. Affirmer offers the Work as-is and makes no representations or warranties
#   of any kind concerning the Work, express, implied, statutory or otherwise,
#   including without limitation warranties of title, merchantability, fitness
#   for a particular purpose, non infringement, or the absence of latent or
#   other defects, accuracy, or the present or absence of errors, whether or not
#   discoverable, all to the greatest extent permissible under applicable law.

#   c. Affirmer disclaims responsibility for clearing rights of other persons
#   that may apply to the Work or any use thereof, including without limitation
#   any person's Copyright and Related Rights in the Work. Further, Affirmer
#   disclaims responsibility for obtaining any necessary consents, permissions
#   or other rights required for any use of the Work.

#   d. Affirmer understands and acknowledges that Creative Commons is not a
#   party to this document and has no duty or obligation with respect to this
#   CC0 or use of the Work.

# For more information, please see
# <http://creativecommons.org/publicdomain/zero/1.0/>