import re
from openstates.utils.actions import Rule, BaseCategorizer

# These are regex patterns that map to action categories.
_categorizer_rules = (
    Rule([u'Amendment #\\S+ \\((?P<legislator>.+?)\\) bundle YES adopted'],
         [u'amendment-passage']),
    Rule([u'(?i)Signed by (the )Governor(.*)'], [u'executive-signature']),
    Rule([u'Accompanied (by )?(?P<bill_id>[SH]\\S+)'], []),
    Rule([u'Discharged to the committee on (?P<committees>.+)'],
         [u'referral-committee']),
    Rule([u'(?i)Amendment #\\d+ adopted'], [u'amendment-passage']),
    Rule([u'Amendment #\\d+ \\((?P<legislator>.+?)\\) rejected',
    u'(?i)amendment.+?rejected'],
         [u'amendment-failure']),
    Rule([u'(?is)Amendment \\S+ withdrawn'], [u'amendment-withdrawal']),
    Rule([u'Amendment #\\S+ \\((?P<legislator>.+?)\\) Pending'],
         [u'amendment-introduction']),
    Rule([u'(?P<bill>[HS]\\d+)'], []),
    Rule([u'(?i)Amendment \\(#\\d+\\) adopted'], [u'amendment-passage']),
    Rule([u'(?i)with veto'], [u'executive-veto']),
    Rule([u'reported favorably by committee'], [u'committee-passage-favorable']),
    Rule([u'Accompan\\S+ .+?(?P<bill_id>[SH]\\S+)'], []),
    Rule([u'(?i)Amendment \\d+ pending'], [u'amendment-deferral']),
    Rule([u'Read,'], [u'reading-1']),
    Rule([u'(?i)Amendment #\\S+ \\((?P<legislator>.+?)\\)\\s+-\\s+rejected',
    u'(?i)Amendment \\d+ rejected',
    u'Amendment #?\\S+ \\((?P<legislator>.+?)\\) rejected'],
         [u'amendment-failure']),
    Rule([u'Amended \\((?P<legislator>.+?)\\) ',
    u'Amendment #?\\S+ \\((?P<legislator>.+?)\\) adopted'],
         [u'amendment-passage']),
    Rule([u'(?i)read.{,10}second'], [u'reading-2']),
    Rule([u'Amendment #\\d+ \\((?P<legislator>.+?)\\) pending'],
         [u'amendment-introduction']),
    Rule([u'Enacted'], [u'passage']),
    Rule([u'Amendment #\\S+ \\((?P<legislator>.+?)\\) Adopted',
    u'Accompanied a study order, (see )?(?P<bill_id>[SH]\\S+)'],
         []),
    Rule([u'passed over veto'], [u'veto-override-passage']),
    Rule([u'(?i)Read third'], [u'reading-3']),
    Rule([u'Bill Filed'], [u'introduction']),
    Rule([u'(?i)Amendment #\\S+ rejected'], [u'amendment-failure']),
    Rule([u'laid aside'], [u'amendment-deferral']),
    Rule([u'(?i)Amendment \\(#\\d+\\) rejected'], [u'amendment-failure']),
    Rule([u'(?i)amendment.+?adopted'], [u'amendment-passage']),
    Rule([u'Adopted, (see )?(?P<bill_id>[SH]\\S+)'], []),
    Rule([u'(?is)Amendment \\(\\d+\\) rejected'], [u'amendment-failure']),
    Rule([u'(?P<yes_votes>\\d+) YEAS.+?(?P<no_votes>\\d+) NAYS'], []),
    Rule([u'Passed to be engrossed'], [u'passage']),
    Rule([u'Amendment #\\d+ \\((?P<legislator>.+?)\\) adopted'],
         [u'amendment-passage']),
    Rule([u'Amendment #\\S+ \\((?P<legislator>.+?)\\) Rejected'],
         [u'amendment-failure']),
    Rule([u'referred to (?P<committees>.+)'], []),
    Rule([u'Amended by'], [u'amendment-passage']),
    Rule(['Committee recommended ought to pass'], ['committee-passage-favorable']),
    Rule([u'Amendment #\\S+ \\((?P<legislator>.+?)\\) bundle NO rejected'],
         [u'amendment-failure']),
    Rule([u'(?is)Amendment \\(\\d+\\) adopted'], [u'amendment-passage']),
    Rule([u'(?i)(Referred|Recommittedra) to (?P<committees>committee on.+)'],
         [u'referral-committee']),
    Rule([u'Accompanied a new draft, (see )?(?P<bill_id>[SH]\\S+)'], []),
    Rule([u'(?i)Amendment #\\S+ \\((?P<legislator>.+?)\\) bundle NO rejected'],
         [u'amendment-failure']),
    Rule([u'(?i)(Referred|Recommittedra) to (?P<chamber>\\S+) (?P<committees>committee on.+)'],
         [u'referral-committee']),
    Rule(['Committee recommended ought NOT'], ['committee-passage-unfavorable']),
    Rule([u'(?i)(Referred|Recommittedra) (to|from)( the)? (?P<chamber>\\S+) (?P<committees>committee on.+)'],
         [u'referral-committee']),
    Rule([u'(?i)Amendment #\\d+ rejected'], [u'amendment-failure']),
    Rule([u'(?i)Amendment \\d+ adopted'], [u'amendment-passage']),
    Rule([u'Committee of Conference appointed \\((?P<legislator>.+?)\\)'], [])
    )


class Categorizer(BaseCategorizer):
    rules = _categorizer_rules
