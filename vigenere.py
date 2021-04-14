from string import uppercase
from operator import itemgetter
 
def vigenere_decrypt(target_freqs, input):
    nchars = len(uppercase)
    ordA = ord('A')
    sorted_targets = sorted(target_freqs)
 
    def frequency(input):
        result = [[c, 0.0] for c in uppercase]
        for c in input:
            result[c - ordA][1] += 1
        return result

    cleaned = [ord(c) for c in input.upper() if c.isupper()]
    best_len = 6   # Found using Friedman's Test
    best_corr = 101.46937 
    for i in xrange(2, len(cleaned) // 20):
        pieces = [[] for _ in xrange(i)]
        for j, c in enumerate(cleaned):
            pieces[j % i].append(c)

    pieces = [[] for _ in xrange(best_len)]
    for i, c in enumerate(cleaned):
        pieces[i % best_len].append(c)
 
    freqs = [frequency(p) for p in pieces]
    key = ""
    for fr in freqs:
        fr.sort(key=itemgetter(1), reverse=True)
 
        m = 0
        max_corr = 0.0
        for j in xrange(nchars):
            corr = 0.0
            c = ordA + j
            for frc in fr:
                d = (ord(frc[0]) - c + nchars) % nchars
                corr += frc[1] * target_freqs[d]
 
            if corr > max_corr:
                m = j
                max_corr = corr
 
        key += chr(m + ordA)
 
    r = (chr((c - ord(key[i % best_len]) + nchars) % nchars + ordA)
         for i, c in enumerate(cleaned))
    
    decoded = "".join(r)
    return (key, decoded)
 
 
def main():
    encoded = """
        HRXJR EWTHM RLYOH XSLWT HWRFK IGCZA LHXYR EDYFI IAANZ BFHJS HZJRH TXGSR
JFBZK RWNGU JNKTA CIGWE GSVNJ MBMJV GNXRG YGRBH XFSTN LENFD BNJZG OGMNV
DLVID RLOTH VAVAL NYRKP TWVPJ AYNUR DIUYI NLEES UVNEL CEGGS TNLEF STNDB
KPAYI RSNWJ CHFGX MZGKE EZZAL OMBVC DAGYK RNEGN YRFCT MJVFI PCCYL RTHJZ
ATGYN QSTTU SBMTM BVCDA GYKFU OFJFF ATBIE NKLHH XNKIM MRALE GHREW MTCEF
HOBHK RVTHQ REVET LKUOI MBKUW ALMZF LFKID FEAEF KUJUL NVEKN HMGNU EVLRS
LHTMV IWRUY VAKOV FFFWT HMRGM RGSFH UAGNY VFKHZ TNKSB HZNKT AYWVJ SMMRG
MRGJI BTELU ZQDIG XRFHI EEVEU ALMZA APKIA RUTLW ZRFTB MKGZE BIENF DGYLG
JAEGR FKSIY TGJOF YKRJW BFCNU TTMKU WNHMV BXTAY JCSCX WINXT WCIRU TESJN
EPECE TLHXW FZHOL CKVGN THUFL RNWKH JEHZK UWAMG FFHHX LVFGM XNYVF GMBRG
UAGNS RVOGY WEGMH LSVLS TCUUM NMYIJ SIMYK RSMEY RQXOK NYRKP XWKEG MXNVE
ATPCC YSLLI ZANEL NZTST XNYRJ IGAIN ANIBV AGMXH FAVIL WFIWR XXSLF ALUJI
GYTAV EEILM ZBFIG NYRWA KFPAA NXNVR FEBAY GAELQ YRJEB NRCHE TLVQL HTNKU
WRBHX FOEKY INANB HXQGW GGRGW RBUCB FTAYG YSNXN RAVCT OJVFG VBRAY ELCEG
ZETND BKPAY IRLHX MGRUT KIDRL EKQZY DAMNV ZHTMI ZANEL NZTST XQYNL MTNVE
AAECJ SJOFN YRJIG AJNFD PBRGE AMYIV SLBMG NJTHZ KUWAM GFFHH XLVOM TVIEG
SCMQZ YDQNC TXDYU YCBKT HHTRL HXMGN UEVLR SLEGN VEKST NLEFS TNDBK PAYIR
STTBZ TZSIY VQSBH OKGOO FCEHL ELFRG WRVUJ FANBQ ZYDBN LENFD WCJVF TXAIN
LEVID CDEMY CLSNR NINUE LIWVL WBFCZ WLMXL RLOMB VUWAM UEQZI ZBGEW SLOIR
GFMBV TAAGN GYSNX NJUGS MCCRS TFIJC ZEKYK UASPC CYDID YCLZA IJVAS RHOEQ
KIQNY VJTRU DRSSM YIALI FYWBJ TAYJC SCXWI NXTUO KTAVX HKUWT BGVVL TTEVF
XOKNY RKIZH RYLOK YRPZE TLKUO EPCCY JEVYZ IWTAI JRDAL NSVLS HZUNL ACOJG
TEYII RWIZB KNELH HXNXT XLTNK SBHZV KGHHV GZELJ RPWCK UWGKF BHRYK IZHRY
OIEFS RDIDY RAWCA IJNAD XUIYE ABTVP SSLCE VHRHD VPLMT HRTWR BNNVD LKUUV
STXUT EGSLN YRKOE UIFQS MYDSG RGYRE DYTHY BMRTH UNZAE ZRSLE KWRFK IGCZG
KEEZY NKGHH V"""
 
    english_frequences = [
        0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,
        0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
        0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
        0.00978, 0.02360, 0.00150, 0.01974, 0.00074]
 
    (key, decoded) = vigenere_decrypt(english_frequences, encoded)
    print ("Key:", key)
    print ("Text:", decoded)
 
main()
