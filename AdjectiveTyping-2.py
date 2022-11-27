#requires download of nltk in python
import os
import nltk
from nltk.corpus import *
import string

def main():
    print("\nHere are the corpora built into nltk:")
    for h in os.listdir(nltk.data.find("corpora")):
        if '.zip' not in h:
            print(h)
    print()
    chosen_corpora = input("Enter corpora name (copy the name EXACTLY as listed): ")
    function_string = "nltk.corpus." + chosen_corpora + ".fileids()"
    print("\nHere are the options of corpora from", chosen_corpora + ": \n")
    for corpus in eval(function_string):
        print(str(corpus))
    print()
    text_function = chosen_corpora + ".raw(str(input('Enter text file name (with .txt): ')))"
    text = eval(text_function)
    tokens = nltk.word_tokenize(text)
    tagged_corpora = nltk.pos_tag(tokens)
    update_corpora = ""

    # need to edit above code ^ what are we outputting for text files?
    # remember "such" shouldn't be categorized as an adjective
    # case check
    
    # being, in the abstract
    existence_1 = ["existing", "existent", "extant", "afloat", "afoot", "current", "prevalent", "undestroyed", "real", "actual", "positive", \
        "absolute", "true", "substantial", "substantive", "self-existing", "self-existent", "essential", "well-founded", "well-grounded", \
        "unideal", "unimagined", "authentic", "inexistent", "nonexistent", "negative", "blank", "missing", "omitted", "absent", "insubstantial", \
        "shadowy", "spectral", "visionary", "unreal", "potential", "virtual", "baseless", "unsubstantial", "vain", "unborn", "uncreated", \
        "unbegotten", "unconceived", "unproduced", "unmade", "perished", "annihilated", "extinct", "exhausted", "gone", "lost", "vanished", \
        "departed", "defunct", "fabulous", "ideal", "supposititious"]
    
    # being, in the concrete
    existence_2 = ["substantive", "substantial", "hypostatic", "personal", "bodily", "tangible", "corporeal", "unsubstantial", "baseless", \
        "groundless", "ungrounded", "visionary", "immaterial", "spectral", "dreamy", "shadowy", "ethereal", "airy", "gossamery", "illusory", \
        "insubstantial", "unreal", "vacant", "vacuous", "empty", "eviscerated", "blank", "hollow", "nominal", "null", "inane"]

    # formal existence
    existence_3 = ["subjective", "intrinsic", "intrinsical", "fundamental", "normal", "implanted", "inherent", "essential", "natural", "innate", \
        "inborn", "inbred", "ingrained", "inwrought", "genetous", "haematobious", "syngenic", "radical", "incarnate", "thoroughbred", "hereditary", \
        "inherited", "immanent", "congenital", "congenite", "connate", "ingenerate", "ingenite", "indigenous", "instinctive", "inward", "internal", \
        "virtual", "characteristic", "special", "indicative", "invariable", "incurable", "incorrigible", "ineradicable", "fixed", "objective", \
        "extrinsic", "extrinsical", "extraneous", "foreign", "modal", "adventitious", "ascititious", "adscititious", "incidental", "accidental", \
        "nonessential", "contingent", "fortuitous", "implanted", "ingrafted", "inculcated", "infused", "outward", "apparent", "external"]

    # modal existence
    existence_4 = ["conditional", "modal", "formal", "structural", "organic", "circumstantial", "given", "conditional", "provisional", "critical", \
        "modal", "contingent", "incidental", "adventitious", "extrinsic", "limitative"]
    
    # absolute relation
    relation_1 = ["relative", "correlative", "cognate", "referable", "related", "connected", "implicated", "associated", "affiliated", "approximative", \
        "approximating", "proportional", "proportionate", "proportionable", "allusive", "comparable", "like", "relevant", "apt", "applicable", \
        "equiparant", "irrelative", "irrespective", "unrelated", "arbitrary", "independent", "unallied", "unconnected", "disconnected", "adrift", \
        "isolated", "insular", "extraneous", "strange", "alien", "foreign", "outlandish", "exotic", "incommensurable", "heterogeneous", \
        "unconformable", "irrelevant", "inapplicable", "purpose", "impertinent", "inapposite", "misplaced", "intrusive", "remote", "far-fetched", \
        "forced", "detached", "segregate", "disquiparant", "multifarious", "discordant", "incidental", "parenthetical", "episodic", "related", \
        "akin", "consanguineous", "family", "allied", "collateral", "cognate", "agnate", "connate", "kindred", "affiliated", "fraternal", \
        "allied", "german", "reciprocal", "mutual", "commutual", "correlative", "reciprocative", "interrelated", "alternate", "interchangeable", \
        "interdependent", "international", "complemental", "complementary", "identical", "self", "ilk", "selfsame", "homoousian", "coincide", \
        "coalescent", "coalescing", "indistinguishable", "one", "equivalent", "equal", "unaltered", "contrary", "contrarious", "contrariant", \
        "opposite", "counter", "converse", "reverse", "opposed", "antithetical", "contrasted", "antipodean", "antagonistic", "opposing", \
        "conflicting", "inconsistent", "contradictory", "negative", "hostile", "differing", "different", "diverse", "heterogeneous", "multifarious", \
        "polyglot", "distinguishable", "dissimilar", "varied", "modified", "diversified", "various", "divers", "variform", "daedal", "other", \
        "another", "unequal", "unmatched", "distinctive", "characteristic", "discriminative", "distinguishing", "incommensurable", "incommensurate"]
    
    # continuous relation
    relation_2 = ["uniform", "homogeneous", "homologous", "consistent", "connatural", "monotonous", "even", "invariable", "regular", "unchanged", \
        "undeviating", "unvaried", "unvarying", "unsegmented", "diversified", "varied", "irregular", "uneven", "rough"," multifarious", "multiform"]

    # partial relation
    relation_3 = ["similar", "resembling", "like", "alike", "twin", "analogous", "analogical", "parallel", "so", "homoiousian", "connatural", \
        "congener", "consanguineous", "approximate", "near", "close", "mock", "pseudo", "simulating", "representing", "exact", "true", "lifelike", \
        "faithful", "dissimilar", "unlike", "disparate", "divergent", "class", "unmatched", "unique", "new", "novel", "unprecedented", "original", \
        "diversified", "imitated", "mock", "mimic", "paraphrastic", "literal", "imitative", "secondhand", "imitable", "aping", "apish", "mimicking", \
        "unimitated", "uncopied", "unmatched", "unparalleled", "inimitable", "unique", "original", "creative", "inventive", "untranslated", \
        "exceptional", "rare", "unexampled", "varied"," modified", "diversified", "faithful", "lifelike", "similar", "close", "conscientious", \
        "unoriginal", "imitative", "derivative"]
    
    # general relation
    relation_4 = ["agreeing", "suiting", "accordant", "concordant", "consonant", "congruous", "consentaneous", "correspondent", "congenial", \
        "coherent", "becoming", "harmonious", "reconcilable", "conformable", "consistent", "compatible", "proportionate", "commensurate", \
        "apt", "apposite", "pertinent", "pat", "happy", "felicitous", "germane", "applicable", "relevant", "admissible", "fit", "adapted", \
        "appropriate", "seasonable", "sortable", "suitable", "idoneous", "deft", "meet", "expedient", "disagreeing", "discordant", "discrepant", \
        "hostile", "antagonistic", "repugnant", "incompatible", "irreconcilable", "inconsistent", "unconformable", "exceptional", "intrusive", \
        "incongruous", "disproportionate", "disproportionated", "inharmonious", "unharmonious", "inconsonant", "unconsonant", "divergent", "repugnant", \
        "inapt", "unapt", "inappropriate", "improper", "unsuited", "unsuitable", "inapplicable", "unfit", "unfitting", "unbefitting", "unbecoming", \
        "illtimed", "unseasonable", "inadmissible", "inapposite", "irrelevant", "uncongenial", "ill-assorted", "ill-sorted", "mismatched", "misjoined", \
        "misplaced"," misclassified", "unaccommodating", "irreducible", "incommensurable", "uncommensurable", "unsympathetic"]
    
    # simple quantity
    quantity_1 = ["quantitative", "some", "any", "aught", "more", "less", "few", "comparative", "gradual", "limit"]

    # comparative quantity
    quantity_2 = ["equal", "even", "level", "monotonous", "coequal", "symmetrical", "coordinate", "equiparant", "equivalent", "tantamount", \
        "indistinguishable", "quits", "homologous", "synonymous", "resolvable", "convertible", "equipollent", "equiponderant", "equiponderous", \
        "equibalanced", "equalized", "drawn", "isochronal", "isochronous", "isoperimetric", "isoperimetrical", "isobath", "isobathic", "unequal", \
        "uneven", "disparate", "partial", "unbalanced", "overbalanced", "top-heavy", "lopsided", "biased", "skewed", "disquiparant", "mean", "middle", \
        "average", "neutral", "mediocre", "middle-class", "commonplace", "unimportant", "compensating", "compensatory", "countervailing", "equivalent", \
        "equal", "great", "greater", "large", "considerable", "fair", "big", "huge", "Herculean", "cyclopean", "ample", "abundant", "enough", \
        "full", "intense", "strong", "sound", "passing", "heavy", "plenary", "deep", "high", "signal", "world-wide", "widespread", "far-famed", \
        "extensive", "wholesale", "many", "goodly", "noble", "precious", "mighty", "sad", "grave", "heavy", "serious", "arrant", "downright", "utter", \
        "uttermost", "crass", "gross", "arch", "profound", "intense", "consummate", "rank", "uninitiated", "red-hot", "desperate", "glaring", "flagrant", \
        "stark", "staring", "thorough-paced", "thoroughgoing", "roaring", "thumping", "extraordinary", "important", "unsurpassed", "supreme", "complete", \
        "august", "grand", "dignified", "sublime", "majestic", "repute", "vast", "immense", "enormous", "extreme", "inordinate", "excessive", "extravagant", \
        "exorbitant", "outrageous", "preposterous", "unconscionable", "swinging", "monstrous", "overgrown", "towering", "stupendous", "prodigious", \
        "astonishing", "incredible", "marvelous", "unlimited", "infinite", "unapproachable", "unutterable", "indescribable", "ineffable", "unspeakable", \
        "inexpressible", "fabulous", "undiminished", "unabated", "unreduced", "unrestricted", "absolute", "positive", "stark", "decided", "unequivocal", \
        "essential", "perfect", "finished", "remarkable", "marked", "pointed", "veriest", "noteworthy", "renowned", "small", "little", "diminutive", \
        "minute", "fine", "inconsiderable", "paltry", "unimportant", "faint", "weak", "slender", "light", "slight", "scanty", "scant", "limited", \
        "meager", "insufficient", "sparing", "few", "low", "so-so", "middling", "tolerable", "halfway", "moderate", "modest", "tender", "subtle", \
        "inappreciable", "evanescent", "infinitesimal", "homeopathic", "atomic", "corpuscular", "microscopic", "molecular", "subatomic", "mere", "simple", \
        "sheer", "stark", "bare", "dull", "petty", "shallow", "stolid", "ungifted", "unintelligent", "superior", "greater", "major", "higher", "exceeding", \
        "great", "distinguished", "ultra", "vaulting", "supreme", "greatest", "utmost", "paramount", "preeminent", "foremost", "crowning", "first-rate", \
        "important", "excellent", "unrivaled", "peerless", "matchless", "unparagoned", "unparalleled", "unequalled", "unapproached", "unsurpassed", \
        "superlative", "inimitable", "facile", "princeps", "incomparable", "sovereign", "culminating", "topmost", "transcendent", "transcendental", \
        "enlarged", "expanded", "inferior", "smaller", "small", "minor", "less", "lesser", "deficient", "minus", "lower", "subordinate", "secondary", \
        "secondrate", "imperfect", "sub", "subaltern", "least", "smallest", "little", "small", "lowest", "diminished", "decreased", "reduced"," contracted", \
        "unimportant", "increased", "undiminished", "additional", "added", "unincreased", "decreased", "decreasing"]
    
    # conjunctive quantity
    quantity_3 = ["added", "additional", "supplemental", "supplementary", "suppletory", "subjunctive", "adjectitious", "adscititious", "ascititious", \
        "additive", "extra", "accessory", "subtracted"," subtractive", "additional", "alate", "alated", "winged", "remaining", "left", "residual", \
        "residuary", "over", "odd", "unconsumed", "sedimentary", "surviving", "net", "exceeding", "outlying", "outstanding", "superfluous", "redundant", \
        "mixed", "implex", "composite", "half-and-half", "linsey-woolsey", "chowchow", "hybrid", "mongrel", "heterogeneous", "motley", "variegated", \
        "miscellaneous", "promiscuous", "indiscriminate", "miscible", "simple", "uniform", "homogeneous", "single", "pure", "sheer", "neat", "unmixed", \
        "unmingled", "unblended", "uncombined", "uncompounded", "elementary", "undecomposed", "unadulterated", "unsophisticated", "unalloyed", "untinged", \
        "unfortified", "incomplex", "exclusive", "joined", "joint", "conjoint", "conjunct", "corporate", "compact", "firm", "fast", "close", "tight", \
        "taut", "taught", "secure", "set", "intervolved", "inseparable", "indissoluble", "insecable", "severable", "disjoined", "discontinuous", "multipartite", \
        "abstract", "disjunctive", "secant", "isolated", "insular", "separate", "disparate", "discrete", "apart", "asunder", "loose", "free", "unattached", \
        "unannexed", "unassociated", "unconnected", "distinct", "adrift", "straggling", "rift", "reft", "scissile", "divisible", "discerptible", "partible", \
        "separable", "cohesive", "adhesive", "adhering", "cohering", "tenacious", "tough", "sticky", "united", "unseparated", "unsessile", "inseparable", \
        "inextricable", "infrangible", "compact", "dense", "nonadhesive", "immiscible", "incoherent", "detached", "loose", "baggy", "slack", "lax", \
        "relaxed", "flapping", "streaming", "disheveled", "segregated", "unconsolidated", "uncombined", "noncohesive", "combined", "impregnated", "ingrained", \
        "imbued", "inoculated", "decomposed", "catalytic", "analytical", "resolvent", "separative", "solvent"]
    
    # concrete quantity
    quantity_4 = ["whole", "total", "integral", "entire", "complete", "one", "individual", "unbroken", "intact", "uncut", "undivided", "unsevered", "unclipped", \
        "uncropped", "unshorn", "seamless", "undiminished", "undemolished", "undissolved", "undestroyed", "unbruised", "indivisible", "indissoluble", \
        "indissolvable", "indiscerptible", "wholesale", "sweeping", "comprehensive", "fractional", "fragmentary", "sectional", "aliquot", "divided", "multifid", \
        "disconnected", "partial", "complete", "entire", "whole", "perfect", "full", "good", "absolute", "thorough", "plenary", "solid", "undivided", "all-sided", \
        "exhaustive", "radical", "sweeping", "thorough-going", "dead", "regular", "consummate", "unmitigated", "sheer", "unqualified", "unconditional", "free", \
        "abundant", "sufficient", "brimming", "brimful", "topful", "topfull", "saturated", "crammed", "replete", "redundant", "fraught", "laden", "full-laden", \
        "full-fraught", "full-charged", "heavy laden", "completing", "supplemental", "supplementary", "ascititious", "incomplete", "imperfect", "unfinished", \
        "uncompleted", "complete", "defective", "deficient", "wanting", "lacking", "failing", "hollow", "meager", "lame", "half-and-half", "perfunctory", "sketchy", \
        "crude", "unprepared", "mutilated", "garbled", "docked", "lopped", "truncated", "proceeding", "containing", "constituting", "excluding", "exclusive", \
        "excluded", "unrecounted", "inadmissible", "forming", "inclusive", "extraneous", "foreign", "alien", "ulterior", "tramontane", "ultramontane", "excluded", \
        "inadmissible", "exceptional"]

    # order in general
    order_1 = ["orderly", "regular", "neat", "tidy", "well-regulated", "correct", "methodical", "uniform", "symmetrical", "shipshape", "businesslike", "systematic", \
        "unconfused", "confuse", "arranged", "disorderly", "orderless", "irregular", "desultory", "anomalous", "unconformable", "acephalous", "deranged", "aimless", \
        "disorganized", "straggling", "unmethodical", "immethodical", "unsymmetric", "unsystematic", "untidy", "slovenly", "dislocated", "promiscuous", "indiscriminate", \
        "chaotic", "anarchical", "unarranged", "arrange", "confused", "deranged", "topsy-turvy", "inverted", "shapeless", "disjointed", "troublous", "riotous", "violent" \
        "complex", "gnarled", "knarled", "complex", "complexed", "intricate", "complicated", "perplexed", "involved", "raveled", "entangled", "knotted", "tangled", \
        "inextricable", "irreducible", "arranged", "embattled", "methodical", "orderly", "regular", "systematic", "deranged", "syncretic", "syncretistic", "mussy", \
        "messy", "flaky", "random", "unordered"]

    # consecutive order
    order_2 = ["preceding", "precedent", "antecedent", "anterior", "prior", "before", "former", "foregoing", "beforementioned", "abovementioned", "aforementioned", \
        "aforesaid", "said", "precursory", "precursive", "prevenient", "preliminary", "prefatory", "introductory", "prelusive", "prelusory", "proemial", "preparatory", \
        "succeeding", "sequent", "subsequent", "consequent", "sequacious", "proximate", "next", "consecutive", "continuity", "alternate", "amoebean", "latter", "posterior", \
        "precursory", "prelusive", "prelusory", "preludious", "proemial", "introductory", "prefatory", "prodromous", "inaugural", "preliminary", "precedent", "prior", \
        "beginning", "initial", "initiatory", "initiative", "inceptive", "introductory", "incipient", "proemial", "inaugural", "inchoate", "inchoative", "embryonic", \
        "rudimental", "primogenial", "primeval", "primitive", "primordial", "old", "aboriginal", "natal", "nascent", "first", "foremost", "leading", "maiden", "begun", \
        "ending", "final", "terminal", "definitive", "crowning", "completing", "last", "ultimate", "hindermost", "rear", "caudal", "vergent", "conterminate", "conterminous", \
        "conterminable", "ended", "settled", "decided", "over", "conclusive", "penultimate", "unbegun", "uncommenced", "fresh", "middle", "medial", "mesial", "mean", "mid", \
        "median", "average", "middlemost", "midmost", "mediate", "intermediate", "interjacent", "equidistant", "central", "mediterranean", "equatorial", "homocentric", \
        "continuous", "continued", "consecutive", "progressive", "gradual", "serial", "successive", "immediate", "unbroken", "entire", "linear", "uninterrupted", "unintermitting", \
        "unremitting", "unrelenting", "perseverence", "perennial", "evergreen", "constant", "discontinuous", "unsuccessive", "broken", "interrupted", "dicousu", "disconnected", \
        "unconnected", "discrete", "disjunctive", "fitful", "irregular", "spasmodic", "desultory", "intermitting", "occasional", "intermittent", "alternate", "recurrent", \
        "periodic"]

    # collective order
    order_3 = ["assembled", "dense", "serried", "crowded", "teeming", "swarming", "populous", "fasciculated", "cumulative", "unassembled", "assemble", "dispersed", "sparse", \
        "dispread", "broadcast", "sporadic", "widespread", "epidemic", "general", "adrift", "stray", "disheveled", "streaming"]
    
    # distributive order
    order_4 = ["included", "including", "inclusive", "congener", "congenerous", "encircling", "general", "generic", "collective", "broad", "comprehensive", "sweeping", \
        "encyclopedical", "widespread", "dispersed", "universal", "catholic", "catholical", "common", "worldwide", "ecumenical", "oecumenical", "transcendental", "prevalent", \
        "prevailing", "rife", "epidemic", "besetting", "Pan-American", "Anglican", "Pan-Hellenic", "Pan-Germanic", "slavic", "panharmonic", "every", "all", "unspecified", \
        "impersonal", "customary", "habitual", "special", "particular", "individual", "specific", "proper", "personal", "original", "private", "respective", "definite", \
        "determinate", "especial", "certain", "esoteric", "endemic", "partial", "party", "peculiar", "appropriate", "several", "characteristic", "diagnostic", "exclusive", \
        "singular", "exceptional", "idiomatic", "idiotypical", "typical", "this", "that", "yon", "yonder"]
    
    # order as regards categories
    order_5 = ["normal", "natural", "unexceptional", "common", "usual", "frequency", "polymorphous", "multiform", "multifold", "multifarious", "multigenerous", "multiplex", \
        "heterogeneous", "diversified", "dissimilar", "various", "varied", "variform", "manifold", "many-sided", "variegated", "motley", "mosaic", "epicene", "indiscriminate", \
        "desultory", "irregular", "mixed", "different", "assorted", "mingled", "odd", "diverse", "divers", "jumbled", "confused", "discordant", "inharmonious", "unmatched", \
        "unrelated", "nonuniform", "omniform", "omnigenous", "omnifarious", "protean", "form", "conformable", "regular", "well-regulated", "regulated", "orderly", "symmetric", \
        "conventional", "customary", "ordinary", "common", "habitual", "usual", "everyday", "workaday", "naturalized", "typical", "normal", "nominal", "formal", "canonical", \
        "orthodox", "sound", "strict", "rigid", "positive", "uncompromising", "Procrustean", "shipshape", "technical", "illustrative", "uncomformable", "exceptional", "abnormal", \
        "abnormous", "anomalous", "anomalistic", "irregular", "arbitrary", "teratogenic", "lawless", "informal", "aberrant", "stray", "wandering", "wanton", "peculiar", "exclusive", \
        "unnatural", "eccentric", "egregious", "misplaced", "funny", "unusual", "unaccustomed", "uncustomary", "unwonted", "uncommon", "rare", "curious", "odd", "extraordinary", \
        "strange", "monstrous", "wonderful", "unexpected", "unaccountable", "outre", "remarkable", "noteworthy", "queer", "quaint", "nondescript", "unfashionable", "fantastic", \
        "grotesque", "bizarre", "outlandish", "exotic", "preternatural", "denaturalized", "heterogeneous", "heteroclite", "amorphous", "mongrel", "amphibious", "epicene", "half-blood", \
        "hybrid", "androgynous", "androgynal", "asymmetric", "adelomorphous", "bisexual", "hermaphrodite", "monoclinous", "qualified", "singular", "unique", "one-of-a-kind", \
        "newfangled", "novel", "non-classical", "original", "unconventional", "unfamiliar", "undescribed", "unprecedented", "unparalleled", "unexampled"]
    
    # number, in the abstract
    number_1 = ["numeral", "complementary", "divisible", "aliquot", "reciprocal", "prime", "fractional", "decimal", "figurate", "incommensurable", "proportional", "exponential", \
        "logarithmic", "logometric", "differential", "fluxional", "integral", "totitive", "positive", "negative", "rational", "irrational", "surd", "radical", "real", "complex", \
        "imaginary", "finite", "infinite", "impossible", "numeral", "numerical", "arithmetical", "analytic", "algebraic", "statistical", "numerable", "computable", "calculable", \
        "commensurable", "commensurate", "incommensurable", "incommensurate", "innumerable", "unfathomable", "infinite", "cadastral"]

    # determinate number
    # if "demi" or "semi" or "hemi" in prefix of word, it counts as number adj
    # if "tri" or "tris" in prefix of word, it counts as number adj
    number_2 = ["one", "sole", "single", "solitary", "unitary", "individual", "apart", "alone", "kithless", "unaccompanied", "unattended", "solus", "single-handed", "singular", "odd", \
        "unique", "unrepeated", "azygous", "first", "last", "isolated", "disjoined", "insular", "monospermous", "unific", "uniflorous", "unifoliate", "unigenital", "uniliteral", \
        "unijocular", "unimodal", "unimodular", "lone", "lonely", "lonesome", "desolate", "dreary", "insecable", "inseverable", "indiscerptible", "compact", "indivisible", "atomic", \
        "irresolvable", "accompanying", "concomitant", "fellow", "twin", "joint", "accessory", "attendant", "obbligato", "two", "twin", "dual", "dualistic", "double", "binary", "binomial", \
        "twin", "biparous", "dyadic", "conduplicate", "duplex", "biduous", "binate", "diphyletic", "dispermic", "unijugate", "tete-a-tete", "coupled", "conjugate", "both", "double", \
        "doubled", "bicipital", "bicephalous", "bidental", "bilabiate", "bivalve", "bivalvular", "bifold", "biform", "bilateral", "bifarious", "bifacial", "twofold", "two-sided", \
        "disomatous", "duplex", "double-faced", "double-headed", "twin", "duplicate", "ingeminate", "second", "bisected", "cloven", "cleft", "bipartite", "biconjugate", "bicuspid", \
        "bifid", "bifurcous", "bifurcate", "bifurcated", "distichous", "dichotomous", "furcular", "semi", "demi", "hemi", "three", "triform", "trinal", "trinomial", "tertiary", "ternary", \
        "triune", "triarch", "triadie", "triple", "treble", "triple", "tern", "ternary", "triplicate", "threefold", "trilogistic", "third", "trinal", "trine", "trifid", "trisected", \
        "tripartite", "trichotomous", "trisulcate", "Triadelphous", "triangular", "tricuspid", "tricapsular", "tridental", "tridentate", "tridentiferous", "trifoliate", "trifurcate", \
        "trigonal", "trigrammic", "trigrammatic", "tripetalous", "tripodal", "tripodic", "triquetral", "triquetrous", "four", "quaternary", "quaternal", "quadratic", "quartile", "tetract", \
        "tetractic", "tetractinal", "tetrad", "tetragonal", "square", "quadrate", "fourfold", "quadrable", "quadrumanous", "quadruple", "quadruplicate", "quadrible", "fourth", "quadrifoliate", \
        "quadrifoliolate", "quadrigeminal", "quadrigeminate", "quadriplanar", "quadriserial", "quartered", "quadrifid", "quadripartite", "rectangular", "five", "quinary", "quintuple", "fifth", \
        "senary", "sextuple", "sixth", "seventh", "septuple", "octuple", "eighth", "ninefold", "ninth", "tenfold", "decimal", "denary", "decuple", "tenth", "eleventh", "duodenary", "duodenal", \
        "twelfth", "thirteenth", "vicesimal", "vigesimal", "twentieth", "twenty-fourth", "vicenary", "vicennial", "centuple", "centuplicate", "centennial", "centenary", "centurial", "secular", \
        "hundredth", "thousandth", "quinquefid", "quinquelateral", "quinquepartite", "quinqevalent", "pentavalent", "quinquarticular", "octifid", "decimal", "tenth", "tithe", "duodecimal", \
        "twelfth", "sexagesimal", "sexagenary", "hundredth", "centesimal", "millesimal"]
    
    # indeterminate number
    number_3 = ["plural", "some", "several", "few", "certain", "fractional", "fragmentary", "inconsiderable", "negligible", "infinitesimal", "many", "several", "sundry", "divers", "various", \
        "Briarean", "hundred", "thousand", "myriad", "million", "quadrillion", "nonillion", "numerous", "numerose", "profuse", "manifold", "multiplied", "multitudinous", "multiple", \
        "multinominal", "teeming", "populous", "peopled", "crowded", "thick", "studded", "galore", "thick", "coming", "many", "more", "endless", "infinite", "few", "scant", "scanty", "thin", \
        "rare", "scattered", "spotty",  "exiguous", "infrequent", "reduced", "unrepeated", "repeated", "repetitional", "repetitionary", "recurrent", "recurring", "frequent", "incessant", \
        "redundant", "pleonastic", "monotonous", "harping", "iterative", "recursive", "unvaried", "mocking", "chiming", "retold", "aforesaid", "aforenamed", "above-mentioned", "above-said", \
        "habitual", "another", "infinite", "immense", "numberless", "countless", "sumless", "measureless", "innumerable", "immeasurable", "incalculable", "illimitable", "inexhaustible", \
        "interminable", "unfathomable", "unapproachable", "exhaustless", "indefinite", "incomprehensible", "limitless", "endless", "boundless", "termless", "untold", "unnumbered", "unmeasured",
        "unbounded", "unlimited", "illimited", "perpetual"]

    # absolute time
    time_1 = ["continuing", "permanent", "durable", "horary", "hourly", "annual", "periodical", "elapsing", "aoristic", "progressive", "durable", "lasting", "permanent", "endless", "chronic", \
        "long-standing", "intransient", "intransitive", "intransmutable", "persistent", "lifelong", "livelong", "longeval", "long-lived", "macrobiotic", "diuturnal", "evergreen", "perennial", \
        "sempervirent", "sempervirid", "unrelenting", "unintermitting", "unremitting", "perpetual", "lingering", "protracted", "prolonged", "long-pending", "long-winded", "slow", "transient", \
        "transitory", "transitive", "passing", "evanescent", "fleeting", "cursory", "short-lived", "ephemeral", "flying", "fugacious", "fugitive", "shifting", "slippery", "spasmodic", \
        "instantaneous", "momentaneous", "temporal", "temporary", "provisional", "provisory", "deciduous", "perishable", "mortal", "precarious", "unstable", "insecure", "impermanent", "brief", \
        "quick", "brisk", "extemporaneous", "haste", "sudden", "momentary", "instantaneous", "perpetual", "eternal", "everduring", "everlasting", "ever-living", "ever-flowing", "continual", \
        "sempiternal", "coeternal", "endless", "unending", "ceaseless", "incessant", "uninterrupted", "indesinent", "unceasing", "endless", "unending", "interminable", "unfading", "evergreen", \
        "amaranthine", "neverending", "never-dying", "never-fading", "deathless", "immortal", "undying", "imperishable", "instantaneous", "momentary", "sudden", "immediate", "instant", "abrupt", \
        "discontinuous", "precipitous", "precipitant", "precipitate", "subitaneous", "hasty", "rapid", "speedy", "quick", "fast", "fleet", "swift", "lively", "blitz", "velocity", "chronological", \
        "chronometrical", "chronogrammatical", "cinquecento", "quattrocento", "trecento", "misdated" "undated", "overdue"]

    # relative time
    time_2 = ["prior", "previous", "preceding", "precedent", "anterior", "antecedent", "pre-existing", "pre-existent", "former", "foregoing", "aforementioned", "before-mentioned", "abovementioned", \
        "aforesaid", "said", "introductory", "precursory", "subsequent", "posterior", "following", "after", "later", "succeeding", "postliminious", "postnate", "postdiluvial", "postdiluvian", \
        "puisne", "posthumous", "future", "afterdinner", "postprandial", "present", "actual", "instant", "current", "existing", "extant", "present-day", "up-to-date", "up-to-the-moment", "aoristic", \
        "indefinite", "synchronous", "synchronal", "synchronic", "synchronical", "synchronistical", "simultaneous", "coexisting", "coincident", "concomitant", "concurrent", "coeval", "coevous", \
        "contemporary", "contemporaneous", "coetaneous", "coeternal", "isochronous", "future", "coming", "impending", "next", "near", "eventual", "ulterior", "expectation", "past", "gone", "over", \
        "bygone", "foregone", "elapsed", "lapsed", "preterlapsed", "expired", "has-been", "extinct", "antediluvian", "antebellum", "exploded", "forgotten", "irrecoverable", "obsolete", "old", "former", \
        "pristine", "quondam", "ci-devant", "late", "ancestral", "foregoing", "last", "latter", "recent", "preterperfect", "preterpluperfect", "retrospective", "retroactive", "archaeological", "new", \
        "novel", "recent", "fresh", "green", "young", "evergreen", "raw", "immature", "unsettled", "yeasty", "virgin", "untried", "unhandseled", "untrodden", "untrod", "unbeaten", "fire-new", \
        "span-new", "late", "modern", "neoteric", "hypermodern", "nouveau", "new-born", "nascent", "neonatal", "new-fashioned", "new-fangled", "new-fledged", "brand-new", "fashionable", "in", "hip", \
        "vernal", "renovated", "sempervirent", "sempervirid", "old", "ancient", "antique", "time-honored", "venerable", "elder", "eldest", "firstborn", "prime", "primitive", "primeval", "primigenous", \
        "paleolontological", "paleontologic", "paleoanthropological", "paleoanthropic", "paleolithic", "primordial", "primordinate", "aboriginal", "beginning", "diluvian", "antediluvian", "protohistoric", \
        "prehistoric", "antebellum", "colonial", "precolumbian", "patriarchal", "preadamite", "paleocrystic", "fossil", "paleozoolical", "paleozoic", "preglacial", "antemundane", "archaic", "classic", \
        "medieval", "Pre-Raphaelite", "ancestral", "black-letter", "immemorial", "traditional", "prescriptive", "customary", "inveterate", "rooted", "antiquated", "rococo", "after-age", "obsolete", "stale", \
        "old-fashioned", "old-world", "exploded", "passe", "senile", "crumbling", "deteriorated", "secondhand", "Archeozoic", "Proterozoic", "Paleozoic", "Mesozoic", "Cenozoic", "Precambrian", "Cambrian", \
        "Ordovician", "Silurian", "Devonian", "Mississippian", "Pennsylvanian", "Permian", "Triassic", "Jurassic", "Cretaceous", "Tertiary", "Paleogene", "Neocene", "Quaternary", "Paleocene", "Eocene", \
        "Oligocene", "Miocene", "Pliocene", "Pleistocene", "Recent", "recent", "matin", "matutinal", "vernal", "vespertine", "autumnal", "nocturnal",  "young", "youthful", "juvenile", "green", "callow", \
        "budding", "sappy", "puisne", "beardless", "underage", "younger", "junior", "hebetic", "unfledged", "aged", "old", "elderly", "geriatric", "senile", "matronly", "anile", "ripe", "mellow", "declining", \
        "waning", "gray", "gray-headed", "hoar", "hoary", "venerable", "time-worn", "antiquated", "passe", "effete", "decrepit", "superannuated", "wrinkled", "doting", "imbecile", "older", "elder", "eldest", \
        "senior", "firstborn", "ancestral", "patriarchal", "ancient", "gerontic", "infantine", "infantile", "puerile", "boyish", "girlish", "childish", "babyish", "kittenish", "baby", "newborn", "unfledged", \
        "new-fledged", "callow", "adolescent", "pubescent", "mature", "middle-aged", "manly", "virile", "adult", "womanly", "matronly", "marriageable", "nubile", "early", "prime", "forward", "prompt", "active", \
        "summary", "premature", "precipitate", "precocious", "prevenient", "anticipatory", "rath", "sudden", "instantaneous", "unexpected", "near", "immediate", "late", "tardy", "slow", "behindhand", "serotine", \
        "belated", "postliminious", "posthumous", "backward", "unpunctual", "untimely", "delayed", "postponed", "dilatory", "slow", "delayed", "timely", "seasonable", "punctual", "prompt", "opportune", "timely", \
        "well-timed", "timeful", "seasonable", "providential", "lucky", "fortunate", "happy", "favorable", "propitious", "auspicious", "critical", "suitable", "ill-timed", "mistimed", "ill-fated", "ill-omened", \
        "ill-starred", "untimely", "unseasonable", "inopportune", "timeless", "intrusive", "untoward", "unlucky", "inauspicious", "infelicitous", "unbefitting", "unpropitious", "unfortunate", "unfavorable", \
        "unsuited", "inexpedient", "unpunctual", "late", "premature", "early"]
    
    # recurrent time
    time_3 = ["frequent", "thickcoming", "incessant", "perpetual", "continual", "steady", "constant", "thick", "uniform", "repeated", "customary", "habit", "regular", "normal", "conformable", "common", "everyday", \
        "usual", "ordinary", "familiar", "old-hat", "boring", "well-known", "trivial", "unfrequent", "infrequent", "rare", "few", "scarce", "unprecedented", "periodic", "periodical", "serial", "recurrent", \
        "cyclical", "rhythmical", "recurring", "intermittent", "remittent", "alternate", "hourly", "diurnal", "daily", "quotidian", "tertian", "weekly", "hebdomadal", "hebdomadary", "biweekly", "fortnightly", \
        "bimonthly", "catamenial", "monthly", "menstrual", "yearly", "annual", "biennial", "triennial", "centennial", "secular", "paschal", "lenten", "regular", "steady", "punctual", "irregular", "uncertain", \
        "unpunctual", "capricious", "desultory", "fitful", "flickering", "rambling", "rhapsodical", "spasmodic", "immethodical", "unmethodical", "variable"]
    
    # simple change
    change_1 = ["changed", "newfangled", "changeable", "transitional", "modifiable", "alterative", "stable", "persisting", "permanent", "established", "unchanged", "change", "renewed", "intact", "inviolate", \
        "persistent", "monotonous", "uncheckered", "unfailing", "undestroyed", "unrepealed", "unsuppressed", "conservative", "prescriptive", "old", "stationary", "continuing", "uninterrupted", "unintermitting", \
        "unvarying", "unshifting", "unreversed", "unstopped", "unrevoked", "unvaried", "sustained", "undying", "perpetual", "inconvertible", "convertible", "resolvable", "transitional", "naturalized", "reverting", \
        "regressive", "revulsive", "reactionary", "retrorse", "unrecognizable", "revolutionary", "substituted", "ersatz", "phony", "vicarious", "subdititious", "interchanged", "reciprocal", "mutual", "commutative", \
        "interchangeable", "intercurrent", "combinatorial", "recombinant"]
    
    # complex change
    change_2 = ["changeable", "changeful", "changing", "mutable", "variable", "checkered", "protean", "proteiform", "versatile", "unstaid", "inconstant", "unsteady", "unstable", "unfixed", "unsettled", "fluctuating", \
        "restless", "agitated", "erratic", "fickle", "irresolute", "capricious", "inconsonant", "fitful", "spasmodic", "vibratory", "vagrant", "wayward", "desultory", "afloat", "alternating", "alterable", "plastic", \
        "mobile", "transient", "wavering", "unchangeable", "immutable", "unaltered", "unalterable", "constant", "permanent", "invariable", "undeviating", "stable", "durable", "perennial", "diuturnal", "fixed", \
        "steadfast", "firm", "fast", "steady", "balanced", "confirmed", "valid", "fiducial", "immovable", "irremovable", "riveted", "rooted", "settled", "established", "vested", "incontrovertible", "stereotyped", \
        "indeclinable", "tethered", "anchored", "moored", "deep-rooted", "ineradicable", "inveterate", "obstinate", "transfixed", "aground", "stranded", "stuck", "jammed", "unremovable", "quiescent", "deterioration", \
        "indefeasible", "irretrievable", "intransmutable", "incommutable", "irresoluble", "irrevocable", "irreversible", "reverseless", "inextinguishable", "irreducible", "indissoluble", "indissolvable", "indestructible", \
        "undying", "imperishable", "incorruptible", "indelible", "indeciduous", "insusceptible", "happening", "doing", "current", "afloat", "afoot", "incidental", "eventful", "stirring", "bustling", "memorable", \
        "momentous", "signal", "impending", "destined", "happen", "coming", "instant", "near", "imminent", "brewing", "preparing", "forthcoming", "expected", "horizon", "future", "unborn", "futurity", "pregnant", \
        "producing"]

    # constancy of sequence in events
    causation_1 = ["caused", "causal", "original", "primary", "primitive", "primordial", "aboriginal", "protogenal", "radical", "embryonic", "embryotic", "seminal", "germinal", "connate", "derivative", "hereditary", \
        "telegonous", "attributed", "attributable", "effect", "putative", "ecbatic", "casual", "fortuitous", "accidental", "adventitious", "causeless", "incidental", "contingent", "uncaused", "undetermined", \
        "indeterminate", "random", "statistical", "possible", "unintentional"]
    
    # connection between cause and effect
    causation_2 = ["powerful", "puissant", "potential", "capable", "able", "cogent", "valid", "efficient", "productive", "effective", "effectual", "efficacious", "adequate", "competent", "multipotent", "plenipotent", \
        "omnipotent", "almighty", "forcible", "energetic", "influential", "productive", "powerless", "impotent", "unable", "incapable", "incompetent", "inefficient", "ineffective", "inept", "unfit", "unfitted", \
        "unqualified", "disqualified", "unendowed", "inapt", "unapt", "crippled", "disabled", "armless", "harmless", "unarmed", "weaponless", "defenseless", "unfortified", "indefensible", "vincible", "pregnable", \
        "untenable", "paralytic", "paralyzed", "palsied", "imbecile", "nerveless", "sinewless", "marrowless", "pithless", "lustless", "emasculate", "disjointed", "unnerved", "unhinged", "water-logged", "rudderless", \
        "exhausted", "shattered", "demoralized", "graveled", "helpless", "unfriended", "fatherless", "nugatory", "inoperative", "ineffectual", "failing", "inadequate", "inefficacious", "useless", "strong", "mighty", \
        "vigorous", "forcible", "hard", "adamantine", "stout", "robust", "sturdy", "hardy", "powerful", "potent", "puissant", "valid", "resistless", "irresistible", "invincible", "impregnable", "unconquerable", \
        "indomitable", "dominating", "inextinguishable", "unquenchable", "incontestable", "overpowering", "overwhelming", "powerful", "sufficient", "sovereign", "able-bodied", "athletic", "Herculean", "Cyclopean", \
        "Atlantean", "muscular", "brawny", "wiry", "well-knit", "broad-shouldered", "sinewy", "strapping", "stalwart", "gigantic", "manly", "man-like", "manful", "masculine", "male", "virile", "unweakened", "unallayed", \
        "unwithered", "unshaken", "unworn", "unexhausted", "stubborn", "thick-ribbed", "deep-rooted", "weak", "feeble", "debile", "impotent", "relaxed", "unnerved", "sapless", "strengthless", "powerless", "weakly", \
        "unstrung", "flaccid", "adynamic", "asthenic", "nervous", "soft", "effeminate", "feminate", "womanly", "frail", "fragile", "shattery", "flimsy", "unsubstantial", "insubstantial", "gimcrack", "gingerbread", \
        "rickety", "creaky", "creaking", "cranky", "craichy", "drooping", "tottering", "broken", "lame", "withered", "shattered", "shaken", "crazy", "shaky", "palsied", "decrepit", "languid", "poor", "infirm", "faint", \
        "faintish", "sickly", "disease", "dull", "slack", "evanid", "spent", "short-winded", "effete", "weather-beaten", "decayed", "rotten", "worn", "seedy", "languishing", "wasted", "washy", "unstrengthened", \
        "unsupported", "unaided", "unassisted", "aidless", "defenseless", "cantilevered", "support", "colorless"]
    
    # power in operation
    causation_3 = ["produced", "producing", "prolific", "creative", "formative", "genetic", "genial", "genital", "pregnant", "enceinte", "teeming", "parturient", "puerperal", "puerperous", "digenetic", "heterogenetic", \
        "oogenetic", "xenogenetic", "ectogenous", "gamic", "haematobious", "sporogenous", "sporophorous", "architectonic", "destroyed", "perishing", "extinct", "all-destroying", "all-devouring", "all-engulfing", \
        "destructive", "subversive", "ruinous", "devastating", "incendiary", "deletory", "destroying", "suicidal", "deadly", "killing", "reproduced", "renascent", "reappearing", "reproductive", "suigenetic", "paternal", \
        "parental", "maternal", "family", "ancestral", "linear", "patriarchal", "filial", "diphyletic", "productive", "prolific", "teeming", "teemful", "fertile", "fruitful", "frugiferous", "fruit-bearing", "fecund", \
        "luxuriant", "pregnant", "uberous", "procreant", "procreative", "generative", "life-giving", "spermatic", "multiparous", "omnific", "propagable", "parturient", "producing", "profitable", "useful", "unproductive", \
        "acarpous", "inoperative", "barren", "addled", "infertile", "unfertile", "unprolific", "arid", "sterile", "unfruitful", "infecund", "fallow", "teemless", "issueless", "fruitless", "unprofitable", "useless", "null", \
        "void", "operative", "efficient", "efficacious", "practical", "effectual", "acting", "doing", "strong", "energetic", "forcible", "active", "intense", "deep-dyed", "severe", "keen", "vivid", "sharp", "acute", \
        "incisive", "trenchant", "brisk", "rousing", "irritation", "poignant", "virulent", "caustic", "corrosive", "mordant", "harsh", "stringent", "double-edged", "double-shotted", "double-distilled", "drastic", \
        "escharotic", "racy", "pungent", "potent", "powerful", "radioactive", "inert", "inactive", "passive", "torpid", "sluggish", "dull", "heavy", "flat", "slack", "tame", "slow", "blunt", "unreactive", "lifeless", \
        "dead", "uninfluential", "latent", "dormant", "smoldering", "unexerted", "violent", "vehement", "warm", "acute", "sharp", "rough", "rude", "ungentle", "bluff", "boisterous", "wild", "brusque", "abrupt", "waspish", \
        "impetuous", "rampant", "turbulent", "disorderly", "blustering", "raging", "troublous", "riotous", "tumultuary", "tumultuous", "obstreperous", "uproarious", "extravagant", "unmitigated", "ravening", "inextinguishable", \
        "tameless", "frenzied", "insane", "desperate", "rash", "infuriate", "furious", "outrageous", "frantic", "hysteric", "fiery", "flaming", "scorching", "hot", "red-hot", "ebullient", "savage", "fierce", "ferocious", \
        "excited", "unquelled", "unquenched", "unextinguished", "unrepressed", "unbridled", "unruly", "headstrong", "ungovernable", "unappeasable", "immitigable", "unmitigable", "uncontrollable", "incontrollable", \
        "insuppressible", "irrepressible", "orgastic", "orgasmatic", "orgasmic", "spasmodic", "convulsive", "explosive", "detonating", "volcanic", "meteoric", "stormy", "windy", "moderate", "lenient", "gentle", "mild", \
        "mellow", "cool", "sober", "temperate", "reasonable", "measured", "tempered", "calm", "unruffled", "quiet", "tranquil", "still", "slow", "smooth", "untroubled", "tame", "peaceful", "peaceable", "pacific", "halcyon", \
        "unexciting", "unirritating", "soft", "bland", "oily", "demulcent", "lenitive", "anodyne", "hypnotic", "sedative", "antiorgastic", "anaphrodisiac"]

    # indirect power
    causation_4 = ["influential", "effective", "important", "weighty", "prevailing", "prevalent", "rife", "rampant", "dominant", "regnant", "predominant", "hegemonical", "uninfluential", "ineffective", "inconsequential", \
        "nugatory", "unconducing", "unconducive", "powerless", "irrelevant", "tending", "conducive", "liable", "subservient", "instrumental", "useful", "subsidiary", "helping", "liable", "subject", "answerable", "contingent", \
        "incidental", "possible"]
    
    # combinations of causes
    causation_5 = ["concurring", "concurrent", "coinciding", "counteracting", "antagonistic", "conflicting", "retroactive", "renitent", "reactionary", "contrary"]

    # abstract space
    spacegen_1 = ["spacious", "roomy", "extensive", "expansive", "capacious", "ample", "widespread", "vast", "world-wide", "uncircumscribed", "boundless", "infinite", "shoreless", "trackless", "pathless", "extended", "territorial", \
        "local", "parochial", "provincial", "regional"]

    # relative space
    spacegen_2 = ["situate", "situated", "local", "topical", "topographical", "placed", "situate", "posited", "ensconced", "imbedded", "embosomed", "rooted", "domesticated", "unremoved", "moored", "displaced", "unplaced", \
        "unhoused", "unharbored", "unestablished", "unsettled", "houseless", "homeless", "misplaced"]

    # existence in space
    spacegen_3 = ["present", "occupying", "inhabiting", "moored", "resiant", "resident", "residentiary", "domiciled", "ubiquitous", "ubiquitary", "omnipresent", "peopled", "populous", "inhabited", "absent", "away", "nonresident", \
        "gone", "missing", "lost", "wanting", "omitted", "inexistence", "empty", "void", "vacant", "vacuous", "untenanted", "unoccupied", "uninhabited", "tenantless", "barren", "sterile", "desert", "deserted", "devoid", "uninhabitable", \
        "indigenous", "native", "natal", "autochthonal", "autochthonous", "British", "English", "American", "Canadian", "Irish", "Scotch", "Scottish", "Welsh", "domestic", "domiciliated", "domiciled", "naturalized", "vernacular", \
        "domesticated", "domiciliary", "urban", "metropolitan", "suburban", "provincial", "rural", "rustic", "domestic", "cosmopolitan", "palatial", "capsular", "saccular", "sacculated", "recipient", "ventricular", "cystic", "vascular", \
        "vesicular", "cellular", "camerated", "locular", "multilocular", "polygastric", "marsupial", "siliquose", "siliquous"]
    
    # general dimensions
    dimension_1 = ["large", "big", "great", "quantity", "considerable", "bulky", "voluminous", "ample", "massive", "massy", "capacious", "comprehensive", "spacious", "mighty", "towering", "fine", "magnificent", "corpulent", "stout", \
        "fat", "obese", "plump", "squab", "full", "lusty", "strapping", "bouncing", "portly", "burly", "well-fed", "full-grown", "corn-fed", "gram-fed", "stalwart", "brawny", "fleshy", "goodly", "chopping", "jolly", "chub-faced", \
        "chubby-faced", "lubberly", "hulky", "unwieldy", "lumpish", "gaunt", "spanking", "whacking", "whopping", "walloping", "thumping", "thundering", "hulking", "overgrown", "puffy", "swollen", "huge", "immense", "enormous", "mighty", \
        "vast", "vasty", "amplitudinous", "stupendous", "monster", "monstrous", "humongous", "monumental", "elephantine", "jumbo", "mammoth", "gigantic", "gigantean", "giant", "giant-like", "titanic", "prodigious", "colossal", \
        "Cyclopean", "Brobdingnagian", "Bunyanesque", "Herculean", "Gargantuan", "infinite", "immeasurable", "unfathomable", "unplumbed", "inconceivable", "unimaginable", "unheard-of", "little", "small", "minute", "diminutive", \
        "microscopic", "microzoal", "inconsiderable", "unimportant", "exiguous", "puny", "tiny", "wee", "petty", "minikin", "miniature", "pygmy", "pigmy", "elfin", "undersized", "dwarf", "dwarfed", "dwarfish", "spare", "stunted", \
        "limited", "cramp", "cramped", "pollard", "Liliputian", "dapper", "pocket", "portative", "portable", "duodecimo", "dumpy", "squat", "short", "impalpable", "intangible", "evanescent", "imperceptible", "invisible", "inappreciable", \
        "insignificant", "inconsiderable", "trivial", "infinitesimal", "homoeopathic", "atomic", "subatomic", "corpuscular", "molecular", "rudimentary", "rudimental", "embryonic", "vestigial", "weazen", "scant", "scraggy", "scrubby", \
        "thin", "narrow", "granular", "powdery", "shrunk", "brevipennate", "expanded", "larger", "large", "swollen", "expansive", "wide", "widespread", "flabelliform", "overgrown", "exaggerated", "bloated", "fat", "turgid", "tumid", \
        "hypertrophied", "dropsical", "pot-bellied", "swag-bellied", "edematous", "oedematous", "obese", "puffy", "pursy", "blowzy", "bigswoln", "distended", "patulous", "bulbous", "convex", "full-blown", "full-grown", "full-formed", \
        "big", "abdominous", "enchymatous", "rhipidate", "tumefacient", "tumefying", "contracting", "astringent", "shrunk", "contracted", "strangulated", "tabid", "wizened", "stunted", "waning", "neap", "compact", "unexpanded", "expand", \
        "contractile", "compressible", "smaller", "small", "distant", "far", "remote", "telescopic", "distal", "yon", "yonder", "ulterior", "transmarine", "transpontine", "transatlantic", "transalpine", "tramontane", "ultramontane", \
        "ultramundane", "hyperborean", "antipodean", "inaccessible", "unapproached", "unapproachable", "incontiguous", "near", "nigh", "close", "neighboring", "contiguous", "adjacent", "adjoining", "proximate", "proximal", "handy", "home", \
        "intimate", "breachy", "rimose", "rimulose", "contiguous", "touching", "conterminous", "osculatory", "pertingent", "tangential"]

    # linear dimensions
    dimension_2 = ["long", "longsome", "lengthy", "wiredrawn", "outstretched", "lengthened", "sesquipedalian", "words", "interminable", "macrocolous", "linear", "lineal", "longitudinal", "oblong", "unshortened", "shorten", "short", "brief", \
        "curt", "compendious", "compact", "stubby", "scrimp", "shorn", "stubbed", "stumpy", "thickset", "pug", "chunky", "decurtate", "retrousse", "stocky", "squab", "squabby", "squat", "dumpy", "little", "oblate", "concise", "summary", \
        "broad", "wide", "ample", "extended", "discous", "fanlike", "outspread", "outstretched", "latifoliate", "latifolous", "thick", "dumpy", "squab", "squat", "thickset", "narrow", "close", "slender", "thin", "fine", "thread-like", \
        "filament", "finespun", "gossamer", "paper-thin", "taper", "slim", "slight-made", "scant", "scanty", "spare", "delicate", "incapacious", "contracted", "unexpanded", "expand", "emaciated", "lean", "meager", "gaunt", "macilent", \
        "lank", "lanky", "weedy", "skinny", "scrawny" "slinky", "starved", "starveling", "herring", "gutted", "hatchet-faced", "lantern-jawed", "attenuated", "shriveled", "extenuated", "tabid", "marcid", "barebone", "rawboned", "monomolecular", \
        "lamellar", "lamellated", "lamelliform", "layered", "laminated", "laminiferous", "micaceous", "schistose", "schistous", "scaly", "filmy", "membranous", "pellicular", "flaky", "squamous", "foliated", "foliaceous", "stratified", \
        "stratiform", "tabular", "discoid", "spathic", "spathose", "trilamellar", "graphitic", "filamentous", "filamentiferous", "filaceous", "filiform", "fibrous", "fibrillous", "thread-like", "wiry", "stringy", "ropy", "capillary", \
        "capilliform", "funicular", "wire-drawn", "anguilliform", "flagelliform", "hairy", "rough", "taeniate", "taeniform", "taenioid", "venose", "venous", "high", "elevated", "eminent", "exalted", "lofty", "tall", "gigantic", "big", \
        "Patagonian", "towering", "beetling", "soaring", "hanging", "gardens", "elevated", "upper", "highest", "topmost", "high-reaching", "insessorial", "perching", "upland", "moorland", "hilly", "knobby", "mountainous", "alpine", "subalpine", \
        "heaven" "kissing", "cloudtopt", "cloudcapt", "cloudtouching", "aerial", "overhanging", "incumbent", "overlying", "superincumbent", "supernatant", "superimposed", "prominent", "lanky", "thin", "low", "neap", "debased", "nether", "flat", \
        "crouched", "subjacent", "squat", "prostrate", "horizontal", "deep", "deep-seated", "profound", "sunk", "buried", "submerged", "subaqueous", "submarine", "subterranean", "subterraneous", "subterrene", "underground", "bottomless", \
        "soundless", "fathomless", "unfathomed", "unfathomable", "abysmal", "bathycolpian", "benthal", "benthopelagic", "downreaching", "yawning", "knee-deep", "ankle-deep", "shallow", "slight", "superficial", "skin-deep", "ankle-deep", \
        "knee-deep", "shoal", "shoaly", "highest", "high", "top", "topmost", "uppermost", "tiptop", "culminating", "meridian", "meridional", "capital", "head", "polar", "supreme", "supernal", "topgallant", "bottom", "undermost", "nethermost", \
        "fundamental", "vertical", "upright", "erect", "perpendicular", "plumb", "normal", "straight", "bolt", "upright", "rampant", "rectangular", "orthogonal", "horizontal", "level", "even", "plane", "flat", "alluvial", "calm", "smooth", \
        "recumbent", "decumbent", "procumbent", "accumbent", "lying", "prone", "supine", "couchant", "jacent", "prostrate", "recubant", "pendent", "pendulous", "pensile", "hanging", "beetling", "overhanging", "projecting", "dependent", \
        "suspended", "loose", "flowing", "pedunculate", "tailed", "caudate", "supporting", "supported", "fundamental", "dorsigerous", "parallel", "coextensive", "equidistant", "orthogonal", "perpendicular", "rectangular", "uncorrelated", \
        "inverted", "supine", "topsy-turvy", "inverse", "reverse", "contrary", "opposite", "top-heavy", "crossing", "crossed", "matted", "transverse", "cross", "cruciform", "crucial", "retiform", "reticular", "reticulated", "areolar", \
        "cancellated", "grated", "barred", "streaked", "textile", "crossbarred", "cruciate", "palmiped", "secant", "web-footed"]

    # centrical dimensions
    dimension_3 = ["exterior", "external", "outermost", "outward", "outlying", "outside", "outdoor", "extramural", "extralimitary", "extramundane", "superficial", "skin-deep", "frontal", "discoid", "extraregarding", "excentric", "eccentric", \
        "outstanding", "extrinsic", "ecdemic", "exomorphic", "interior", "internal", "inner", "inside", "inward", "intraregarding", "inmost", "innermost", "deep-seated", "gut", "intestine", "intestinal", "inland", "subcutaneous", "abdominal", \
        "coeliac", "endomorphic", "interstitial", "interjacent", "inwrought", "intrinsic", "inclosed", "home", "domestic", "indoor", "intramural", "vernacular", "endemic", "central", "centrical", "middle", "azygous", "axial", "focal", "umbilical", \
        "concentric", "middlemost", "rachidian", "spinal", "vertebral", "covering", "superimposed", "overlaid", "plated", "cutaneous", "dermal", "cortical", "cuticular", "tegumentary", "skinny", "scaly", "squamous", "covered", "imbricated", \
        "loricated", "armor-plated", "ironclad", "undercover", "cowled", "cucullate", "dermatoid", "encuirassed", "hooded", "squamiferous", "tectiform", "vaginate", "lined", "invested", "habited", "dighted", "barbed", "barded", "clad", "costume", \
        "shod", "chausse", "show", "sartorial", "divested", "bare", "naked", "nude", "undressed", "undraped", "denuded", "exposed", "bald", "threadbare", "ragged", "callow", "roofless", "barefoot", "bareback", "barebacked", "leafless", "napless", \
        "hairless", "circumjacent", "circumambient", "circumfluent", "ambient", "surrounding", "circumferential", "suburban", "interjacent", "intercurrent", "intervenient", "intervening", "intermediate", "intermediary", "intercalary", "interstitial", \
        "embolismal", "parenthetical", "episodic", "mediterranean", "intrusive", "embosomed", "merged", "circumscribed", "begirt", "lapt", "embosomed", "imbedded", "embedded", "encysted", "imprisoned", "landlocked", "border", "marginal", "skirting", \
        "labial", "labiated", "marginated", "definite", "conterminate", "conterminable", "terminal", "frontier", "bordering", "fore", "anterior", "front", "frontal", "back", "rear", "hind", "hinder", "hindmost", "hindermost", "postern", "posterior", \
        "dorsal", "after", "caudal", "lumbar", "mizzen", "tergal", "lateral", "sidelong", "collateral", "parietal", "flanking", "skirting", "flanked", "sideling", "many-sided", "multilateral", "bilateral", "trilateral", "quadrilateral", "Eastern", \
        "orient", "oriental", "Levantine", "Western", "occidental", "Hesperian", "opposite", "reverse", "inverse", "converse", "antipodal", "subcontrary", "fronting", "facing", "Northern", "septentrional", "Boreal", "arctic", "Southern", \
        "Austral", "antarctic", "dextral", "right-handed", "dexter", "dextrorsal", "dextrorse", "ambidextral", "ambidextrous", "left-handed", "sinister", "sinistral", "sinistrorsal", "sinistrorse", "sinistrous"]
    
    # general form
    form_1 = ["formed", "plastic", "fictile", "formative", "fluid", "plasmic", "isomorphous", "pleomorphic", "protean", "changeable", "shapeless", "amorphous", "formless", "unformed", "unhewn", "unfashioned", "unshaped", "unshapen", "rough", \
        "rude", "Gothic", "barbarous", "rugged", "symmetrical", "shapely", "finished", "beautiful", "classic", "chaste", "severe", "regular", "uniform", "balanced", "equal", "parallel", "coextensive", "arborescent", "arboriform", "dendriform", \
        "dendroid", "branching", "ramous", "ramose", "filiciform", "filicoid", "subarborescent", "papilionaceous", "fuji-shaped", "fujigata", "distorted", "irregular", "asymmetric", "unsymmetric", "awry", "wry", "askew", "crooked", "crump", \
        "deformed", "harelipped", "misshapen", "misbegotten", "misproportioned", "ill-proportioned", "ill-made", "grotesque", "monstrous", "crooked", "camel-backed", "hump-backed", "hunch-backed", "bunch-backed", "crook-backed", "bandy", \
        "bandy-legged", "bow-legged", "bow-kneed", "knock-kneed", "splay-footed", "club-footed", "round-shouldered", "snub-nosed", "stumpy", "short", "gaunt", "thin", "bloated", "scalene", "simous", "taliped", "talipedic"]
    
    # special form
    form_2 = ["angular", "bent", "crooked", "aduncous", "uncinated", "aquiline", "jagged", "serrated", "falciform", "falcated", "furcated", "forked", "bifurcate", "zigzag", "furcular", "hooked", "dovetailed", "crinkled", "akimbo", \
        "kimbo", "geniculated", "oblique", "fusiform", "wedge-shaped", "cuneiform", "cuneate", "multangular", "oxygonal", "triangular", "trigonal", "trilateral", "quadrangular", "quadrilateral", "foursquare", "rectangular", "square", \
        "multilateral", "polygonal", "cubical", "rhomboid", "rhomboidal", "pyramidal", "curved", "curviform", "curvilineal", "curvilinear", "devex", "devious", "recurved", "recurvous", "crump", "bowed", "vaulted", "hooked", \
        "falciform", "falcated", "semicircular", "crescentic", "sinusoid", "parabolic", "paraboloid", "luniform", "lunular", "semilunar", "conchoidal", "helical", "double-helical", "spiral", "kinky", "cordiform", "cordated", \
        "cardioid", "heart-shaped", "bell-shaped", "boat-shaped", "crescent-shaped", "lens-shaped", "moon-shaped", "oar-shaped", "shield-shaped", "sickle-shaped", "tongue-shaped", "pear-shaped", "fig-shaped", "kidney-shaped", \
        "reniform", "lentiform", "lenticular", "bow-legged", "distorted", "oblique", "circular", "aduncated", "arclike", "arcuate", "arched", "beaked", "bicorn", "bicornuous", "bicornute", "clypeate", "clypeiform", "cymbiform", \
        "embowed", "galeiform", "hamate", "hamiform", "hamous", "hooked", "linguiform", "lingulate", "lobiform", "lunate", "navicular", "peltate", "remiform", "rhamphoid", "rostrate", "rostriferous", "rostroid", "scutate", \
        "scaphoid", "uncate", "unguiculate", "unguiform", "straight", "rectilinear", "rectilineal", "direct", "even", "right", "true", "unbent", "virgate", "undeviating", "unturned", "undistorted", "unswerving", "direct", \
        "inflexible", "laser-straight", "ramrod-straight", "round", "rounded", "circular", "annular", "orbicular", "oval", "ovate", "elliptic", "elliptical", "egg-shaped", "pear-shaped", "cycloidal", "spherical", "convoluted", \
        "winding", "twisted", "tortile", "tortive", "wavy", "undated", "undulatory", "circling", "snaky", "snake-like", "serpentine", "serpent", "anguill", "vermiform", "vermicular", "mazy", "tortuous", "sinuous", "flexuous", \
        "anfractuous", "reclivate", "rivulose", "scolecoid", "sigmoid", "sigmoidal", "spiriferous", "spiroid", "involved", "intricate", "complicated", "perplexed", "labyrinth", "labyrinthic", "labyrinthian", "labyrinthine", \
        "peristaltic", "daedalian", "kinky", "knotted", "wreathy", "frizzly", "crepe", "buckled", "raveled", "spiral", "coiled", "helical", "cochleate", "cochleous", "screw-shaped", "turbinated", "turbiniform", "rotund", "round", \
        "circular", "cylindric", "cylindrical", "cylindroid", "columnar", "lumbriciform", "conic", "conical", "spherical", "spheroidal", "globular", "globated", "globous", "globose", "ovoid", "oviform", "gibbous", "rixiform", \
        "campaniform", "campanulate", "campaniliform", "fungiform", "bead-like", "moniliform", "pyriform", "bulbous"]
    
    # superficial form
    form_3 = ["convex", "prominent", "protuberant", "projecting", "bossed", "embossed", "bossy", "nodular", "bunchy", "clavate", "clavated", "claviform", "hummocky", "moutonne", "mammiliform", "papulous", "papilose", "hemispheric", \
        "bulbous", "bowed", "arched", "bold", "bellied", "tuberous", "tuberculous", "tumous", "cornute", "odontoid", "lentiform", "lenticular", "gibbous", "club-shaped", "hubby", "hubbly", "knobby", "papillose", "saddle-shaped", \
        "selliform", "subclavate", "torose", "ventricose", "verrucose", "salient", "raised", "repousse", "bloated", "expanded", "depressed", "alveolate", "calathiform", "cup-shaped", "dishing", "favaginous", "faveolate", "favose", \
        "scyphiform", "scyphose", "concave", "hollow", "retiring", "retreating", "cavernous", "porous", "infundibul", "infundibular", "infundibuliform", "funnel-shaped", "bell-shaped", "campaniform", "capsular", "vaulted", "arched", \
        "cellular", "spongy", "spongious", "honeycombed", "alveolar", "sintered", "porous", "opening", "sharp", "keen", "acute", "acicular", "aciform", "aculeated", "acuminated", "pointed", "tapering", "conical", "pyramidal", \
        "mucronate", "mucronated", "spindle-shaped", "needle-shaped", "spiked", "spiky", "ensiform", "peaked", "salient", "cusped", "cuspidate", "cuspidated", "cornute", "cornuted", "cornicultate", "prickly", "spiny", "spinous", \
        "spicular", "thorny", "bristling", "muricated", "pectinated", "studded", "thistly", "briary", "craggy", "rough", "snaggy", "digitated", "two-edged", "fusiform", "dentiform", "denticulated", "toothed", "odontoid", "starlike", \
        "stellated", "stelliform", "sagittate", "sagittiform", "arrowheaded", "arrowy", "barbed", "spurred", "acinaciform", "apiculate", "apiculated", "aristate", "awned", "awny", "bearded", "calamiform", "cone-shaped", "coniform", \
        "crestate", "echinate", "gladiate", "lanceolate", "lanciform", "awl", "awl-shaped", "lance-shaped", "awl-shaped", "scimitar-shaped", "sword-shaped", "setarious", "spinuliferous", "subulate", "tetrahedral", "xiphoid", \
        "cutting", "sharp-edged", "knife-edged", "sharpened", "set", "blunt", "obtuse", "dull", "bluff", "edentate", "toothless", "smooth", "polished", "leiodermatous", "slick", "velutinous", "even", "level", "plane", "flat", \
        "sleek", "glossy", "silken", "silky", "lanate", "downy", "velvety", "glabrous", "slippery", "glassy", "lubricous", "oily", "soft", "unwrinkled", "woolly", "feathery", "rough", "uneven", "scabrous", "scaly", "knotted", \
        "rugged", "rugose", "rugous", "knurly", "asperous", "crisp", "salebrous", "gnarled", "unpolished", "unsmooth", "roughhewn", "craggy", "cragged", "crankling", "scraggy", "prickly", "sharp", "arborescent", "leafy", \
        "well-wooded", "feathery", "plumose", "plumigerous", "laciniate", "laciniform", "laciniose", "pappose", "pileous", "pilose", "trichogenous", "trichoid", "tufted", "fimbriated", "hairy", "ciliated", "filamentous", \
        "hirsute", "crinose", "crinite", "bushy", "hispid", "villous", "pappous", "bearded", "pilous", "shaggy", "shagged", "fringed", "befringed", "setous", "setose", "setaceous", "downy", "velvety", "flocculent", "woolly", \
        "lanate", "lanated", "lanuginous", "lanuginose", "tomentose", "fluffy", "notched", "crenate", "crenated", "dentate", "dentated", "denticulate", "denticulated", "toothed", "palmated", "serrated",  "folded", "fluted", \
        "pleated", "furrowed", "ribbed", "striated", "sulcated", "fluted", "canaliculated", "bisulcous", "bisulcate", "bisulcated", "canaliferous", "trisulcate", "corduroy", "unisulcate", "costate", "rimiform", "open", \
        "perforated", "perforate", "ajar", "unclosed", "unstopped", "oscitant", "gaping", "yawning", "patent", "tubular", "cannular", "fistulous", "pervious", "permeable", "foraminous", "vesicular", "vasicular", "porous", \
        "follicular", "cribriform", "honeycombed", "infundibular", "riddled", "tubulous", "tubulated", "piped", "tubate", "opening", "aperient", "closed", "shut", "operculated", "unopened", "unpierced", "imporous", "caecal", \
        "closable", "imperforate", "impervious", "impermeable", "impenetrable", "impassable", "unpassable", "invious", "pathless", "wayless", "untrodden", "untrod", "unventilated", "air-tight", "water-tight", \
        "hermetically-sealed", "tight", "snug"]

    # motion in general
    motion_1 = ["moving", "transitional", "motory", "motive", "shifting", "movable", "mobile", "mercurial", "unquiet", "restless", "changeable", "nomadic", "erratic", "quiescent", "still", "motionless", "moveless", "fixed", \
        "stationary", "immotile", "stock", "still", "sedentary", "untraveled", "stay-at-home", "becalmed", "stagnant", "quiet", "unmoved", "undisturbed", "unruffled", "calm", "restful", "cataleptic", "immovable", "stable", \
        "sleeping", "inactive", "silent", "vegetative", "vegetating", "traveling", "ambulatory", "itinerant", "peripatetic", "roving", "rambling", "gadding", "discursive", "vagrant", "migratory", "monadic", "circumforanean", \
        "circumforaneous", "noctivagrant", "mundivagrant", "locomotive", "wayfaring", "wayworn", "travel-stained", "sailing", "volant", "aerostatic", "seafaring", "nautical", "maritime", "naval", "seagoing", "coasting",\
         "afloat", "navigable", "aerial", "aeronautic", "grallatory", "transferred", "drifted", "movable", "portable", "portative", "mailable", "contagious", "equine", "asinine"]
        
    # degrees of motion
    motion_2 = ["fast", "speedy", "swift", "rapid", "quick", "fleet", "aliped", "nimble", "agile", "expeditious", "express", "active", "flying", "galloping", "light-footed", "nimble-footed", "winged", "eagle-winged", \
        "mercurial", "electric", "telegraphic", "light-legged", "slow", "slack", "tardy", "dilatory", "inactive", "gentle", "easy", "leisurely", "deliberate", "gradual", "insensible", "imperceptible", "glacial", \
        "languid", "sluggish", "slow-paced", "tardigrade", "snail-like", "creeping", "reptatorial"]
    
    # motion conjoined with force
    motion_3 = ["impelling", "impulsive", "impellent", "booming", "dynamic", "dynamical", "impelled", "recoiling", "refluent", "repercussive", "recalcitrant", "reactionary", "retroactive"]

    # motion with reference to direction
    motion_4 = ["directed", "aligned", "direct", "straight", "undeviating", "unswerving", "straightforward", "North", "Northern", "Northerly", "deviating", "aberrant", "errant", "excursive", "discursive", "devious", \
        "desultory", "loose", "rambling", "stray", "erratic", "vagrant", "undirected", "circuitous", "indirect", "zigzag", "crab-like", "leading", "precedent", "subsequent", "next", "succeeding", "following", "advancing", \
        "progressive", "profluent", "advanced", "receding", "retrograde", "retrogressive", "regressive", "refluent", "reflex", "recidivous", "resilient", "crab-like", "balky", "reactionary", "propelled", "propelling", \
        "propulsive", "projectile", "drawing", "tractile", "tractive", "approaching", "approximative", "affluent", "impending", "imminent", "destined",  "receding", "attracting", "attrahent", "attractive", "adducent", \
        "adductive", "centrifugal", "repelling", "repellent", "repulsive", "abducent", "abductive", "centripetal", "converging", "convergent", "confluent", "concurrent", "centripetal", "asymptotical", "asymptotic", \
        "confluxible", "diverging", "divergent", "radiant", "centrifugal", "aberrant", "arriving", "departing", "valedictory", "incoming",  "effused", "outgoing", "admitting", "admitted", "admissable", "absorbent", \
        "emitting", "emitted", "eatable", "edible", "esculent", "comestible", "alimentary", "cereal", "cibarious", "dietetic", "culinary", "nutritive", "nutritious", "gastric", "succulent", "potable", "potulent", \
        "bibulous", "omnivorous", "carnivorous", "herbivorous", "granivorous", "graminivorous", "phytivorous", "ichthyivorous", "omophagic", "omophagous", "pantophagous", "phytophagous", "xylophagous", "inserted", \
        "extracted", "passing", "intercurrent", "endosmosmic", "endosmotic", "surpassing", "unreached", "deficient", "short", "minus", "perfunctory", "neglect",  "rising", "scandent", "buoyant", "supernatant", \
        "superfluitant", "excelsior", "descending", "descendent", "decurrent", "decursive", "labent", "deciduous", "elevated", "stilted", "attollent", "rampant", "depressed", "prostrate", "horizontal", "detrusive", \
        "leaping", "saltatory", "frisky", "turning", "circuitous", "circumforaneous", "circumfluent", "rotating", "rotary", "rotary", "circumrotatory", "trochilic", "vertiginous", "gyratory", "vortical", "vorticose", \
        "evolving", "evolved", "oscillating", "oscillatory", "undulatory", "pulsatory", "libratory", "rectilinear", "vibratory", "vibratile", "pendulous", "shaking", "agitated", "tremulous", "desultory", "subsultory", \
        "saltatoric", "quasative", "shambling", "giddy-paced", "saltatory", "convulsive", "unquiet", "restless"]

    # matter in general
    mattergen_1 = ["material", "bodily", "corporeal", "corporal", "physical", "somatic", "somatoscopic", "sensible", "tangible", "ponderable", "palpable", "substantial", "objective", "impersonal", "nonsubjective", "neuter", \
        "unspiritual", "materialistic", "immaterial", "immateriate", "incorporeal", "incorporal", "incorporate", "unfleshly", "supersensible", "asomatous", "unextended", "unembodied", "disembodied", "extramundane", "unearthly", \
        "pneumatoscopic", "spiritual", "psychical", "personal", "subjective", "nonobjective", "cosmic", "cosmical", "mundane", "terrestrial", "terrestrious", "terraqueous", "terrene", "terreous", "telluric", "earthly", \
        "geotic", "sublunary", "subastral", "solar", "heliacal", "lunar", "celestial", "heavenly", "sphery", "starry", "stellar", "sidereal", "sideral", "astral", "nebular", "uranic", "weighty", "weighing", "ponderous", \
        "ponderable", "lumpish", "lumpy", "cumbersome", "burdensome", "cumbrous", "unwieldy", "massive", "incumbent", "superincumbent", "light", "subtile", "airy", "imponderous", "imponderable", "astatic", "weightless", \
        "ethereal", "sublimated", "gossamery", "suberose", "suberous", "uncompressed", "volatile", "buoyant", "floating", "portable"]

    # solid matter
    inorganic_1 = ["dense", "solid", "solidified", "caseous", "pukka", "coherent", "cohesive", "compact", "close", "serried", "thickset", "substantial", "massive", "lumpish", "impenetrable", "impermeable", "nonporous", "imporous", \
        "incompressible", "constipated", "concrete", "knotted", "knotty", "gnarled", "crystalline", "crystallizable", "thick", "grumous", "stuffy", "undissolved", "unmelted", "unliquefied", "unthawed", "indivisible", \
        "indiscerptible", "infrangible", "indissolvable", "indissoluble", "insoluble", "infusible", "rare", "subtile", "thin", "fine", "tenuous", "compressible", "flimsy", "slight", "light", "cavernous", "spongy", "hollow", \
        "rarefied", "unsubstantial", "uncompact", "incompressed", "rarefiable", "hard", "rigid", "stubborn", "stiff", "firm", "starch", "starched", "stark", "unbending", "unlimber", "unyielding", "inflexible", "tense", "indurate", \
        "indurated", "gritty", "proof", "adamant", "adamantine", "adamantean", "concrete", "stony", "granitic", "calculous", "lithic", "vitreous", "horny", "corneous", "bony", "osseous", "ossific", "cartilaginous", "soft", "tender", \
        "supple", "pliant", "pliable", "flexible", "flexile", "lithe", "lithesome", "lissom", "limber", "plastic", "ductile", "tractile", "tractable", "malleable", "extensile", "sequacious", "inelastic", "aluminous", "remollient", \
        "yielding", "flabby", "limp", "flimsy", "doughy", "spongy", "penetrable", "foamy", "cushiony", "flaccid", "flocculent", "downy", "edematous", "oedematous", "medullary", "argillaceous", "mellow", "elastic", "flexible", \
        "tensile", "spring", "resilient", "renitent", "buoyant", "ductile", "stretchable", "extendable", "unyielding", "inelastic", "inflexible", "soft", "irresilient", "tenacious", "tough", "strong", "resisting", "sequacious", \
        "stringy", "gristly", "cartilaginous", "leathery", "coriaceous", "tough", "obstinate", "unbreakable", "indivisible", "atomic", "brittle", "brash", "breakable", "weak", "frangible", "fragile", "frail", "gimcrack", "shivery", \
        "fissile", "splitting", "lacerable", "splintery", "crisp", "crimp", "short", "structural", "organic", "anatomic", "anatomical", "textural", "textile", "fine-grained", "coarse-grained", "fine", "delicate", "subtile", \
        "gossamery", "filmy", "silky", "satiny", "coarse", "homespun", "rough", "gritty", "smooth", "powdery", "pulverulent", "granular", "mealy", "floury", "farinaceous", "branny", "furfuraceous", "flocculent", "dusty", "sandy", \
        "sabulous", "psammous", "arenose", "arenarious", "arenaceous", "gritty", "efflorescent", "impalpable", "lentiginous", "lepidote", "sabuline", "sporaceous", "sporous", "pulverizable", "friable", "crumbly", "shivery", \
        "pulverized", "attrite", "anatriptic", "attrite", "lubricated", "lubricous"]

    # fluid matter
    inorganic_2 = ["liquid", "fluid", "serous", "juicy", "succulent", "sappy", "ichorous", "fluent", "flowing", "liquefied", "uncongealed", "soluble", "gaseous", "aeriform", "ethereal", "aerial", "airy", "vaporous", "volatile", \
        "evaporable", "flatulent", "liquefied", "liquescent", "liquefiable", "deliquescent", "soluble", "colliquative", "volatilized", "reeking", "volatile", "evaporable", "vaporizable", "bubbly", "effervescent", "boiling", "watery", \
        "aqueous", "aquatic", "hydrous", "lymphatic", "balneal", "diluent", "drenching", "diluted", "weak", "wet", "moist", "flatulent", "effervescent", "windy", "atmospheric", "airy", "aerial", "aeriform", "meteorological", \
        "weatherwise", "moist", "damp", "watery", "madid", "roric", "undried", "humid", "sultry", "wet", "dank", "luggy", "dewy", "roral", "rorid", "roscid", "juicy", "saturated", "swashy", "soggy", "dabbled", "reeking", "dripping", \
        "soaking", "soft", "sodden", "sloppy", "muddy", "swampy", "marshy", "irriguous", "dry", "anhydrous", "arid", "adust", "arescent", "dried", "undamped", "juiceless", "sapless", "sear", "husky", "rainless", "fine", "ehydrated", \
        "dessicated", "oceanic", "marine", "maritime", "pelagic", "pelagian", "seagoing", "hydrographic", "bathybic", "cotidal", "earthy", "continental", "midland", "coastal", "littoral", "riparian", "alluvial", "terrene", "world", \
        "landed", "predial", "territorial", "geophilous", "ripicolous", "lacustrine", "champaign", "alluvial", "campestral", "campestrial", "campestrian", "campestrine", "marsh", "marshy", "swampy", "boggy", "plashy", "poachy", "quaggy", \
        "soft", "muddy", "sloppy", "squashy", "paludal", "moorish", "moory", "fenny", "insular", "seagirt", "archipelagic", "fluent", "diffluent", "profluent", "affluent", "tidal", "flowing", "meandering", "meandry", "meandrous", \
        "fluvial", "fluviatile", "streamy", "showery", "rainy", "pluvial", "stillicidous", "stillatitious", "blowing", "windy", "flatulent", "breezy", "gusty", "squally", "stormy", "tempestuous", "blustering", "boisterous", "violent", \
        "pulmonic", "pulmonary", "vascular"]

    # imperfect fluids
    inorganic_3 = ["semifluid", "semiliquid", "tremellose", "milky", "muddy", "lacteal", "lactean", "lacteous", "lactescent", "lactiferous", "emulsive", "curdled", "thick", "succulent", "uliginous", "gelatinous", "albuminous", \
        "mucilaginous", "glutinous", "glutenous", "gelatin", "mastic", "amylaceous", "ropy", "clammy", "clotted", "viscid", "viscous", "sticky", "tacky", "gooey", "slab", "slabby", "lentous", "pituitous", "mucid", "muculent", "mucous", \
        "gummy", "bubbling", "frothy", "nappy", "effervescent", "sparkling", "mousseux", "frothy", "up", "cloudy", "thunderheaded", "vaporous", "nebulous", "overcast", "pulpy", "pultaceous", "grumous", "baccate", "unctuous", "oily", \
        "oleaginous", "adipose", "sebaceous", "unguinous", "fat", "fatty", "greasy", "waxy", "butyraceous", "soapy", "saponaceous", "pinguid", "lardaceous", "slippery", "resiny", "resinous", "bituminous", "pitchy", "tarry", "asphaltic", \
        "asphaltite"]
    
    # vitality
    organic_1 = ["organic", "organized", "karyoplasmic", "unsegmentic", "vacuolar", "zoogloeic", "zoogloeoid", "inorganic", "inanimate", "inorganized", "lithoidal", "azoic", "mineral", "living", "alive", "breathing", "quick", "animated", \
        "animative", "lively", "active", "yeasty", "vital", "vitalic", "vivifying", "vivified", "viable", "zoetic", "Promethean", "dead", "lifeless", "deceased", "demised", "departed", "defunct", "extinct", "late", "gone", "exanimate", \
        "inanimate", "moribund", "morient", "hippocratic", "booked", "stillborn", "mortuary", "deadly", "killing", "murderous", "slaughterous", "sanguinary", "sanguinolent", "blood-stained", "blood-thirsty", "homicidal", "red-handed", \
        "bloody", "bloody-minded", "ensanguined", "gory", "thuggish", "mortal", "fatal", "lethal", "dead", "deadly", "mortiferous", "lethiferous", "unhealthy", "internecine", "suicidal", "sporting", "piscatorial", "piscatory", \
        "cadaverous", "corpse-like", "unburied", "sapromyiophyllous", "burried", "burial", "funereal", "funebrial", "mortuary", "sepulchral", "cinerary", "elegiac", "necroscopic", "fleshly", "human", "corporeal", "rank", "lush", \
        "vegetable", "vegetal", "vegetive", "animal", "zoological", "equine", "bovine", "vaccine", "canine", "feline", "fishy", "piscatory", "piscatorial", "molluscous", "vermicular", "gallinaceous", "rasorial", "solidungulate", \
        "soliped", "vegetable", "vegetal", "vegetive", "vegitous", "herbaceous", "herbal", "botanic", "sylvan", "silvan", "arborary", "arboreous", "arborescent", "arborical", "woody", "grassy", "verdant", "verdurous", "floral", \
        "mossy", "lignous", "ligneous", "wooden", "leguminous", "vosky", "cespitose", "turf-like", "turfy", "endogenous", "exogenous", "zoological", "botanical", "botanic", "pastoral", "bucolic", "tame", "domestic", "agricultural", \
        "agrarian", "agrestic", "arable", "predial", "rural", "rustic", "country", "horticultural", "human", "mortal", "personal", "individual", "national", "civic", "public", "social", "cosmopolitan", "anthropoid", "male", "masculine", \
        "manly", "virile", "unwomanly", "unfeminine", "his", "female", "feminine", "womanly", "ladylike", "matronly", "maidenly", "wifely", "womanish", "effeminate", "unmanly", "gynecic", "gynaecic", "her", "exy", "erotic", "sexual", \
        "carnal", "sensual", "hot", "horny", "randy", "rutting", "passionate", "lusty", "hot-blooded", "libidinous", "up", "homosexual", "gay", "lesbian", "bisexual"]

    # sensation
    organic_2 = ["sensible", "sensitive", "sensuous", "aesthetic", "perceptive", "sentient", "conscious", "aware", "acute", "sharp", "keen", "vivid", "lively", "impressive", "thin-skinned", "insensible", "unfeeling", "senseless", \
        "impercipient", "callous", "thick-skinned", "pachydermatous", "hard", "hardened", "case-hardened", "proof", "obtuse", "dull", "anaesthetic", "comatose", "paralytic", "palsied", "numb", "dead", "enjoying", "luxurious", "voluptuous", \
        "sensual", "comfortable", "cosy", "snug", "pleasant", "agreeable", "pained", "gouty", "podagric", "torminous", "painful", "aching", "sore", "raw", "tactual", "tactile", "tangible", "palpable", "lambent", "itching", "stereognostic", \
        "titillative", "numb", "benumbed", "deadened", "intangible", "impalpable", "hot", "warm", "mild", "genial", "tepid", "lukewarm", "unfrozen", "thermal", "thermic", "calorific", "fervent", "fervid", "ardent", "aglow", "sunny", "torrid", \
        "tropical", "estival", "canicular", "steamy", "close", "sultry", "stifling", "stuffy", "suffocating", "oppressive", "reeking", "baking", "fiery", "incandescent", "incalescent", "candent", "ebullient", "glowing", "smoking", "live", \
        "dazzling", "blazing", "alight", "afire", "ablaze", "unquenched", "unextinguished", "smoldering", "sudorific", "sweltering", "sweltered", "volcanic", "plutonic", "igneous", "isothermal", "isothermic", "isotheral", "cold", "cool", "chill", \
        "chilly", "icy", "gelid", "frigid", "algid", "fresh", "keen", "bleak", "raw", "inclement", "bitter", "biting", "niveous", "cutting", "nipping", "piercing", "pinching", "clay-cold", "starved", "shivering", "aguish", "frostbitten", \
        "frost-bound", "frost-nipped", "icy", "glacial", "frosty", "freezing", "pruinose", "wintry", "brumal", "hibernal", "boreal", "arctic", "Siberian", "hyemal", "hyperborean", "hyperboreal", "icebound", "unwarmed", "unthawed", "lukewarm", \
        "tepid", "isocheimal", "isocheimenal", "isocheimic", "frozen", "numb", "frost-bitten", "heated", "molten", "sodden", "heating", "adust", "inflammable", "combustible", "diathermal", "diathermanous", "burnt", "volcanic", "radioactive", \
        "cooled", "cooling", "frigorific", "carbonaceous", "combustible", "inflammable", "ncombustible", "nonflammable", "uninflammable", "unflammable", "fireproof", "sapid", "saporific", "gustable", "gustatory", "gustful", "strong", "gamy", \
        "palatable", "bland", "insipid", "tasteless", "gustless", "savorless", "ingustible", "mawkish", "weak", "stale", "flat", "vapid", "fade", "wishy-washy", "mild", "untasted", "pungent", "strong", "full-flavored", "high-tasted", \
        "high-seasoned", "gamy", "sharp", "stinging", "rough", "piquant", "racy", "biting", "mordant", "spicy", "seasoned", "hot", "peppery", "vellicating", "escharotic", "meracious", "acrid", "acrimonious", "bitter", "rough", "sour", \
        "unsavory", "salty", "salt", "saline", "brackish", "briny", "salty", "racy", "indecent", "bitter", "bitterish", "acrid", "acerb", "acerbic", "savory", "delicious", "tasty", "well-tasted", "good", "palatable", "nice", "dainty", \
        "delectable", "toothful", "toothsome", "gustful", "appetizing", "lickerish", "delicate", "exquisite", "rich", "luscious", "ambrosial", "scrumptious", "delightful", "unsavory", "unpalatable", "unsweetened", "unsweet", "ill-flavored", \
        "bitter", "acrid", "acrimonious", "rough", "offensive", "repulsive", "nasty", "sickening", "nauseous", "loathsome", "fulsome", "unpleasant", "sweet", "saccharine", "sacchariferous", "dulcet", "candied", "honied", "luscious", "lush", \
        "nectarious", "melliferous", "sweetened", "sour", "acid", "acidulous", "acidulated", "tart", "crabbed", "acetous", "acetose", "acerb", "acetic", "sourish", "acescent", "subacid", "styptic", "hard", "rough", "odorous", "odoriferous", \
        "smelling", "reeking", "foul-smelling", "strong-scented", "redolent", "graveolent", "nidorous", "pungent", "putrid", "foul", "olfactory", "quick-scented", "inodorous", "onodorate", "scentless", "deodorized", "deodorizing", "fragrant", \
        "aromatic", "redolent", "spicy", "savory", "balmy", "scented", "sweet-smelling", "sweet-scented", "perfumed", "perfumatory", "thuriferous", "muscadine", "ambrosial", "fetid", "strong-smelling", "high", "bad", "strong", "fulsome", \
        "offensive", "noisome", "rank", "rancid", "reasty", "tainted", "musty", "fusty", "frouzy", "olid", "olidous", "nidorous", "smelling", "stinking", "putrid", "suffocating", "mephitic", "empyreumatic", "acrid", "biting", "astringent", \
        "sharp", "harsh", "bitter", "sounding", "soniferous", "sonorous", "sonorific", "resonant", "audible", "distinct", "stertorous", "phonetic", "phonic", "phonocamptic", "silent", "still", "stilly", "noiseless", "soundless", "hushed", \
        "mute", "soft", "solemn", "awful", "deathlike", "inaudible", "faint", "loud", "sonorous", "high-sounding", "big-sounding", "deep", "full", "powerful", "noisy", "blatant", "clangorous", "multisonous", "thundering", "deafening", \
        "trumpet-tongued", "ear-splitting", "ear-rending", "ear-deafening", "piercing", "obstreperous", "rackety", "uproarious", "shrill", "clamorous", "vociferous", "stentorian", "stentorophonic", "inaudible", "low", "dull", \
        "stifled", "muffled", "hoarse", "husky", "gentle", "soft", "faint", "floating", "purling", "flowing", "whispered", "liquid", "soothing", "dulcet", "melodious", "susurrant", "susurrous", "rapping", "rolling", "monotonous", \
        "repeated", "resounding", "resonant", "reverberant", "tinnient", "tintinnabulary", "sonorous", "booming", "deep-toned", "deep-sounding", "deep-mouthed", "vibrant", "hollow", "sepulchral", "gruff", "harsh", "nonresonant", "dead", \
        "dampened", "muffled", "sibilant", "hissing", "wheezy", "sternutative", "creaking", "stridulous", "harsh", "coarse", "hoarse", "horrisonous", "rough", "gruff", "grum", "sepulchral", "hollow" "sharp", "high", "acute", "shrill", \
        "trumpet-toned", "piercing", "ear-piercing", "high-pitched", "high-toned", "cracked", "discordant", "cacophonous", "crying", "clamant", "clamorous", "vociferous", "stentorian", "loud", "open-mouthed", "crying", "blatant",\
        "latrant", "remugient", "mugient", "deep-mouthed", "full-mouthed", "rebellowing", "reboant", "harmonious", "harmonical", "unisonant", "concentual", "symphonizing", "isotonic", "homophonous", "assonant", "ariose", "consonant", \
        "measured", "rhythmical", "diatonic", "chromatic", "enharmonic", "melodious", "musical", "melic", "tuneful", "tunable", "sweet", "dulcet", "canorous", "mellow", "mellifluous", "soft", "clear", "silvery", "euphonious", "euphonic", \
        "euphonical", "symphonious", "enchanting", "pleasure-giving", "fine-toned", "full-toned", "silver-toned", "discordant", "dissonant", "absonant", "tuneless", "unmusical", "untunable", "unmelodious", "immelodious", "unharmonious", \
        "inharmonious", "singsong", "cacophonous", "harsh", "jarring", "musical", "instrumental", "vocal", "choral", "lyric", "operatic", "harmonious", "Wagnerian", "playing", "musical", "hearing", "auditory", "auricular", "acoustic", \
        "phonic", "deaf", "earless", "surd", "deaf-mute", "stunned", "deafened", "inaudible", "shining", "luminous", "luminiferous", "lucid", "lucent", "luculent", "lucific", "luciferous", "light", "lightsome", "bright", "vivid", "splendent", \
        "nitid", "lustrous", "shiny", "beamy", "scintillant", "radiant", "lambent", "sheen", "sheeny", "glossy", "burnished", "glassy", "sunny", "orient", "meridian", "noonday", "tide", "cloudless", "clear", "unclouded", "unobscured", "gairish", \
        "garish", "resplendent", "transplendent", "refulgent", "effulgent", "fulgid", "fulgent", "relucent", "splendid", "blazing", "ablaze", "rutilant", "meteoric", "phosphorescent", "aglow", "actinic", "photogenic", "graphic", "heliographic", \
        "heliophagous", "dark", "darksome", "darkling", "obscure", "tenebrious", "sombrous", "pitchy", "caliginous", "black", "color", "sunless", "lightless", "sunlight", "somber", "dusky", "unilluminated", "illuminate", "nocturnal", "dingy", \
        "lurid", "gloomy", "murky", "murksome", "shady", "umbrageous", "overcast", "dim", "cloudy", "opaque", "darkened", "dark", "pitch", "pit", "benighted", "noctivagant", "noctivagous", "dull", "lackluster", "dingy", "darkish", "dark", "faint", \
        "shadowed", "glassy", "cloudy", "misty", "opaque", "blear", "muggy", "fuliginous", "nebulous", "nebular", "obnubilated", "overcast", "crepuscular", "muddy", "lurid", "leaden", "dun", "dirty", "looming", "pale", "colorless", "confused", \
        "invisible", "self-luminous", "glowing", "phosphoric", "phosphorescent", "fluorescent", "incandescent", "luminescent", "chemiluminescent", "radiant", "light", "shady", "umbrageous", "transparent", "pellucid", "lucid", "diaphanous", \
        "translucent", "tralucent", "relucent", "limpid", "clear", "serene", "crystalline", "clear", "crystal", "vitreous", "transpicuous", "glassy", "hyaline", "hyaloid", "vitreform", "opaque", "impervious", "adiaphanous", "turbid", "thick", \
        "muddy", "opacous", "obfuscated", "fuliginous", "cloud", "hazy", "misty", "foggy", "vaporous", "nubiferous", "muggy", "turbidity", "smoky", "fumid", "murky", "dirty", "turbid", "thick", "muddy", "obfuscated", "fuliginous", "hazy", "misty", \
        "foggy", "vaporous", "nubiferous", "cloudy", "smoky", "fumid", "murky", "dirty", "semitransparent", "translucent", "semipellucid", "semidiaphanous", "semiopacous", "semiopaque", "opalescent", "opaline", "pearly", "milky", "frosted", "nacreous", \
        "colored", "colorific", "tingent", "tinctorial", "chromatic", "prismatic", "full-colored", "high-colored", "deep-colored", "doubly-dyed", "polychromatic", "chromatogenous", "tingible", "bright", "vivid", "intense", "deep", "fresh", "unfaded", \
        "rich", "gorgeous", "gay", "gaudy", "florid", "gay", "garish", "rainbow-colored", "multihued", "showy", "flaunting", "flashy", "raw", "crude", "glaring", "flaring", "discordant", "inharmonious", "mellow", "pastel", "harmonious", "pearly", "sweet", \
        "delicate", "tender", "refined", "uncolored", "color", "colorless", "achromatic", "aplanatic", "etiolate", "etiolated", "hueless", "pale", "pallid", "palefaced", "tallow-faced", "faint", "dull", "cold", "muddy", "leaden", "dun", "wan", "sallow", \
        "dead", "dingy", "ashy", "ashen", "ghastly", "cadaverous", "glassy", "lackluster", "discolored", "light-colored", "fair", "blond", "white", "milk-white", "snow-white", "snowy", "niveous", "candid", "chalky", "hoar", "hoary", "silvery", \
        "argent", "argentine", "canescent", "cretaceous", "lactescent", "whitish", "creamy", "pearly", "fair", "blond", "blanched", "black", "sable", "swarthy", "somber", "dark", "inky", "ebony", "ebon", "atramentous", "jetty", "coal-black", "jet-black", \
        "fuliginous", "pitchy", "sooty", "swart", "dusky", "dingy", "murky", "Ethiopic", "low-toned", "nocturnal", "dark", "nigrescent", "gray", "obscure", "grey", "iron-gray", "dun", "drab", "dingy", "leaden", "livid", "somber", "sad", "pearly", "russet", \
        "roan", "calcareous", "limy", "favillous", "silver", "silvery", "silvered", "ashen", "ashy", "cinereous", "cineritious", "grizzly", "grizzled", "slate-colored", "stone-colored", "mouse-colored", "ash-colored", "cool", "brown", "bay", "dapple", \
        "auburn", "castaneous", "chestnut", "nut-brown", "cinnamon", "russet", "tawny", "fuscous", "chocolate", "maroon", "foxy", "tan", "brunette", "whitey", "brown", "fawn-colored", "snuff-colored", "liver-colored", "brown", "berry", "mahogany", \
        "oak", "khaki", "sun-burnt", "tanned", "red", "reddish", "rufous", "ruddy", "florid", "incarnadine", "sanguine", "rosy", "roseate", "blowzy", "blowed", "burnt", "rubicund", "rubiform", "lurid", "stammell", "blood", "red", "russet", "buff", \
        "murrey", "carroty", "sorrel", "lateritious", "rubineous", "rubricate", "rubricose", "rufulous", "rose-colored", "ruby-colored", "cherry-colored", "claret-colored", "flame-colored", "flesh-colored", "peach-colored", "salmon-colored", \
        "brick-colored", "brick-colored", "dust-colored", "blushing", "erubescent", "reddened", "red", "fire", "scarlet", "warm", "hot", "foxy", "green", "verdant", "glaucous", "olive", "verdurous", "emerald", "greenish", "virent", \
        "unskillful", "new", "inexperienced", "novice", "green", "ill", "sick", "yellow", "aureate", "golden", "flavous", "citrine", "fallow", "fulvous", "fulvid", "sallow", "luteous", "tawny", "creamy", "sandy", "xanthic", "xanthous", \
        "jaundiced", "auricomous", "gold-colored", "citron-colored", "saffron-colored", "lemon-colored", "lemon", "yellow", "sulphur-colored", "amber-colored", "straw-colored", "primrose-colored", "creamcolored", "xanthocarpous", \
        "xanthochroid", "xanthopous", "warm", "advancing", "purple", "violet", "ultraviolet", "plum-colored", "lavender", "lilac", "puce", "mauve", "livid", "blue", "azure", "cerulean", "sky-blue", "sky-colored", "sky-dyed", \
        "cerulescent",  "bluish", "atmospheric", "retiring", "cold", "orange", "ochreous", "orange-colored", "gold-colored", "flame-colored", "copper-colored", "brass-colored", "apricot-colored", "warm", "hot", "glowing", "variegated", \
        "many-colored", "many-hued", "divers-colored", "party-colored", "dichromatic", "polychromatic", "bicolor", "tricolor", "versicolor", "kaleidoscopic", "iridescent", "opaline", "opalescent", "prismatic", "nacreous", "pearly", \
        "shot", "chatoyant", "irisated", "pavonine", "pied", "piebald", "motley", "mottled", "marbled", "paned", "dappled", "clouded", "cymophanous", "mosaic", "tesselated", "plaid", "spotted", "spotty", "punctated", "powdered", \
        "speckled", "freckled", "flea-bitten", "studded", "flecked", "fleckered", "striated", "barred", "veined", "brinded", "brindled", "tabby", "watered", "grizzled", "listed", "embroidered", "daedal", "naevose", "stipiform", \
        "strigose", "striolate", "seeing", "visual", "ocular", "optic", "optical", "ophthalmic", "clear-eyesighted", "eagle-eyed", "hawk-eyed", "lynx-eyed", "keen-eyed", "Argus-eyed", "visible", "blind", "eyeless", "sightless", \
        "visionless", "dark", "stone-blind", "sand-blind", "stark-blind", "undiscerning", "dimsighted", "wall-eyed", "blinded", "dim-sighted", "myopic", "presbyopic", "astigmatic", "moon-eyed", "mope-eyed", "blear-eyed", "goggle-eyed", \
        "gooseberry-eyed", "one-eyed", "monoculous", "half-blind", "purblind", "cock-eyed", "dim-eyed", "mole-eyed", "dichroic", "blind", "winking", "visible", "perceptible", "perceivable", "discernible", "apparent", "unclouded", \
        "unobscured", "obvious", "manifest", "plain", "clear", "distinct", "definite", "well-defined", "well-marked", "recognizable", "palpable", "autoptical", "glaring", "staring", "conspicuous", "stereoscopic", "periscopic", \
        "panoramic", "invisible", "imperceptible", "undiscernible", "indiscernible", "unapparent", "non-apparent", "viewless", "sightless", "inconspicuous", "unconspicuous", "unseen", "see", "covert", "latent", "eclipsed", \
        "dim", "faint", "mysterious", "dark", "obscure", "confused", "indistinct", "indistinguishable", "shadowy", "indefinite", "undefined", "ill-defined", "ill-marked", "blurred", "fuzzy", "misty", "opaque", "delitescent", \
        "hidden", "obscured", "covered", "veiled", "concealed", "apparent", "seeming", "ostensible", "disappearing", "evanescent", "missing", "lost", "gone"]

    # operations of intellect in general
    formation_1 = ["thoughtless", "vegetative", "moronic", "idiotic", "brainless", "thinking", "thoughtful", "pensive", "meditative", "reflective", "museful", "wistful", "contemplative", "speculative", "deliberative", "studious", \
        "sedate", "introspective", "Platonic", "philosophical", "lost", "inattentive", "vacant", "unintellectual", "unideal", "unoccupied", "unthinking", "inconsiderate", "thoughtless", "mindless", "no-brain", "vacuous", "absent", \
        "inattentive", "diverted", "irrational", "narrow-minded", "unconsidered", "incogitable"]
    
    # precursory conditions and operations
    formation_2 = ["curious", "inquisitive", "overcurious", "inquiring", "prying", "snoopy", "nosy", "peering", "prurient", "inquisitorial", "inquisitory", "agape", "expectant", "incurious", "uninquisitive", "indifferent", \
        "impassive", "uninterested", "detached", "aloof", "attentive", "mindful", "observant", "regardful", "observing", "alert", "open-eyed", "absorbed", "rapt", "transfixed", "riveted", "mesmerized", "hypnotized", "breathless", \
        "preoccupied", "inattentive", "watchful", "careful", "breathless", "undistracted", "expectant", "steadfast", "interesting", "engrossing", "mesmerizing", "riveting", "inattentive", "unobservant", "unmindful", "heedless", \
        "unthinking", "unheeding", "undiscerning", "inadvertent", "mindless", "regardless", "respectless", "listless", "indifferent", "blind", "deaf", "bird-witted", "cursory", "percursory", "giddy-brained", "scatter-brained", \
        "hare-brained", "unreflective", "unreflecting", "ecervele", "offhand", "dizzy", "muzzy", "brainsick", "giddy", "wild", "harum-scarum", "rantipole", "highflying", "heedless", "careless", "neglectful", "inconsiderate", \
        "thoughtless", "absent", "abstracted", "distrait", "absentminded", "lost", "rapt", "bemused", "preoccupied", "engrossed", "attentive", "daydreaming", "inexpectant", "napping", "dreamy", "disconcerted", "distracted", \
        "careful", "regardful", "heedful", "particular", "prudent", "cautious", "considerate", "thoughtful", "deliberative", "provident", "prepared", "alert", "active", "sure-footed", "guarded", "awake", "broad", "awake", \
        "vigilant", "watchful", "wakeful", "wistful", "Argus-eyed", "wide-awake", "intelligent", "expectant", "tidy", "orderly", "clean", "accurate", "exact", "scrupulous", "conscientious", "safe", "neglecting", "unmindful", \
        "negligent", "neglectful", "heedless", "careless", "thoughtless", "perfunctory", "remiss", "feebleness", "inconsiderate", "uncircumspect", "incircumspect", "unwary", "unwatchful", "unguarded", "offhand", "supine", \
        "inactive", "inattentive", "insouciant", "indifferent", "imprudent", "reckless", "slovenly", "disorderly", "dirty", "inexact", "erroneous", "improvident", "neglected", "unheeded", "uncared-for", "unperceived", \
        "unseen", "unobserved", "unnoticed", "unnoted", "unmarked", "unattended", "unthought", "unregarded", "unremarked", "unmissed", "shunted", "shelved", "unexamined", "unstudied", "unsearched", "unscanned", "unweighed", \
        "unsifted", "unexplored", "abandoned", "inquiry", "inquisitive", "curious", "requisitive", "requisitory", "catechetical", "inquisitorial", "analytic", "interrogative", "zetetic", "undetermined", "untried", "undecided", \
        "moot", "proposed", "doubtful", "uncertain", "answering", "responsive", "respondent", "conclusive", "experimental", "empirical", "probative", "probatory", "probationary", "provisional", "analytic", "docimastic", \
        "tentative", "unverified", "unproven", "speculative", "untested", "comparative", "metaphorical", "comparable", "incommensurable", "incommensurate", "incomparable", "different", "discriminating", "dioristic", "discriminative", \
        "distinctive", "nice", "indiscriminate", "undistinguished", "indistinguishable", "undistinguishable", "unmeasured", "promiscuous", "undiscriminating", "measuring", "metric", "metrical", "measurable", "perceptible", \
        "noticeable", "detectable", "appreciable", "ponderable", "determinable", "fathomable", "geodetical", "topographic", "topographical", "cartographic", "cartographical"]
    #Roget's Thesaurus for individual adjective typing
    # going to do nested dictionary
    # replace 1's with actual words

    Rogets = {
        "Abstract relations": \
            {"Existence" : 1, "Relation" : 1, "Quantity" : 1, "Order" : 1, "Number" : 1, "Time" : 1, \
                "Change" : 1, "Causation" : 1}, \
        "Space" : \
            {"Space in general" : 1, "Dimensions" : 1, "Form" : 1, "Motion" : 1}, \
        "Matter" : \
            {"Matter in general" : 1, "Inorganic matter": 1, "Organic matter" : 1}, \
                #split into divisions
        "Intellectual faculties" : {"Operations of intellect in general" : 1, \
            "Precursory conditions and operations" : 1, "Materials for reasoning" : 1, "Reasoning processes" : 1, \
                "Results of reasoning" : 1, "Extension of thought" : 1, "Creative thought" : 1, \
                    "Nature of ideas communicated" : 1, "Modes of communication" : 1, "Means of communicating ideas" : 1}, \
                        #split into divisions
        "Voluntary powers" : \
            {"Volition in general" : 1, "Prospective volition" : 1, "Voluntary action" : 1, "Antagonism" : 1, "Results of voluntary action" : 1, \
                "General intersocial volition" : 1, "Special intersocial volition" : 1, "Conditional intersocial volition" : 1, \
                    "Possessive relations" : 1}, \
        "Sentient and moral powers" : \
            {"Affections in general" : 1, "Personal affections" : 1, "Sympathetic affections" : 1, "Moral affections" : 1, "Religious affections" : 1},
    }