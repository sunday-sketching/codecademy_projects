import fetchmaker as fm
import numpy as np
from scipy.stats import binom_test
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import chi2_contingency

rottweiler_tl = fm.get_tail_length("rottweiler")

print(np.mean(rottweiler_tl))
print(np.std(rottweiler_tl))

whippet_rescue = fm.get_is_rescue("whippet")
num_whippet_rescues = np.count_nonzero(whippet_rescue)
num_whippets = np.size(whippet_rescue)
pval = binom_test(num_whippet_rescues, num_whippets, p=0.08)
print(pval)

# pval > 0.05 : Not significant

whippet_wg = fm.get_weight("whippet")
terrier_wg = fm.get_weight("terrier")
pitbull_wg = fm.get_weight("pitbull")
pval2 = f_oneway(whippet_wg, terrier_wg, pitbull_wg).pvalue

print(pval2)

# pval > 0.05 : Not significant

weights = np.concatenate([whippet_wg, terrier_wg, pitbull_wg])
labels = ["Whippet"] * len(whippet_wg) + ["Terrier"] * len(terrier_wg) + ["Pitbull"] * len(pitbull_wg) 

tukey_results = pairwise_tukeyhsd(weights, labels, 0.05)

print(tukey_results)

# Terrier and Whippet 

poodle_colors = fm.get_color("poodle")
shihtzu_colors = fm.get_color("shihtzu")

color_table = [[np.count_nonzero(poodle_colors == "black"),np.count_nonzero(shihtzu_colors == "black")],[np.count_nonzero(poodle_colors == "brown"),np.count_nonzero(shihtzu_colors == "brown")],[np.count_nonzero(poodle_colors == "gold"),np.count_nonzero(shihtzu_colors == "gold")],[np.count_nonzero(poodle_colors == "grey"),np.count_nonzero(shihtzu_colors == "grey")], [np.count_nonzero(poodle_colors == "white"),np.count_nonzero(shihtzu_colors == "white")]]

tstats, pvalue, dfr, ef = chi2_contingency(color_table)

print(pvalue)

# Significant. pvalue < 0.05

