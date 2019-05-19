
class Solution:
    def lastStoneWeight(self, stones) -> int:
        n = len(stones)
        while n > 1:
            n -= 2
            tmp = stones.pop(stones.index(max(stones))) - \
                stones.pop(stones.index(max(stones)))
            if tmp != 0:
                stones.append(tmp)
                n += 1
        return stones[0] if n == 1 else 0

    def removeDuplicates(self, S: str) -> str:
        s = [c+c for c in set(S)]
        while S:
            cnt = 0
            for c in s:
                if c in S:
                    cnt += 1
            if cnt == 0:
                break
            for c in s:
                S = S.replace(c, '')
        return S

    def longestStrChain(self, words) -> int:
        import collections
        words = sorted(words, key=lambda w: len(w))
        f = collections.defaultdict(int)
        ans = 0
        for w in words:
            n = len(w)
            for i in range(n):
                f[w] = max(f[w], f[w[:i]+w[i+1:]]+1)
                ans = max(ans, f[w])
        # print(f)
        return ans


s = Solution()
# print(s.removeDuplicates('abbaca'))
print(s.longestStrChain(["a", "ba", "bca", "bda", "bdca"]))
print(s.longestStrChain(["a", "ba", "bca", "bda", "bdca", "bdcaa", "bdcaaa", "bdcaaaa", "bdcaaaaa", "bdcaaaaaa",
                         "bdcaaaaaab", "bdcaaaaaabb", "bdcaaaaaabbb", "bdcaaaaaabbbb", "bdcaaaaaabbbbb", "bdcaaaaaabbbbbc", "bdcaaaaaabbbbbcc"]))
# print(s.longestStrChain(['f', 'g', 'r', 'z', 'b', 'm', 'o', 'm', 'b', 'uz', 'qz', 'zo', 'ga', 'em', 'mg', 're', 'oh', 'el',
#                          'qf', 'vo', 'gy', 'el', 'kc', 'bm', 'mv', 'qh', 'zv', 'qf', 'wi', 'bu', 'ai', 'gk', 'bek', 'eth', 'nel', 'kuc', 'tmv', 'rey',
#                          'qfe', 'ksg', 'uyz', 'mqz', 'zow', 'aci', 'uvo', 'gym', 'gtu', 'gac', 'znv', 'qfu', 'mjg', 'lel', 'qqh', 'lvz', 'bdm', 'sem',
#                          'ptw', 'bur', 'toh', 'wio', 'glac', 'qqhw', 'fuyz', 'mjhg', 'bexk', 'lvzl', 'dmqz', 'zoow', 'nyhm', 'qqfe', 'wiqo', 'gdtu',
#                          'zsnv', 'arci', 'ptwv', 'zuvo', 'tmgv', 'xfpt', 'ryey', 'vbur', 'qffu', 'gyrm', 'honw', 'vxue', 'tosh', 'semj', 'eqth',
#                          'qksg', 'wkuc', 'sbdm', 'jimp', 'lsel', 'nyel', 'dqzq', 'eqtxh', 'honyw', 'nyepl', 'pdtwv', 'wciqo', 'hdmqz', 'gdigs',
#                          'jimpn', 'qqhwi', 'vburq', 'funyz', 'sibdm', 'gdtua', 'lvzlx', 'zoodw', 'yugag', 'qksgh', 'fetsa', 'mfjhg', 'ftmgv', 'zuvuo',
#                          'ryedy', 'qffuk', 'redna', 'zarci', 'btexk', 'xdqzq', 'wnyhm', 'wkucx', 'vxuce', 'zsnvs', 'gulac', 'gmyrm', 'tosxh', 'qcqfe',
#                          'tufntz', 'wnyhsm', 'gulmac', 'suibdm', 'wciqob', 'mftmgv', 'xdqztq', 'gmyrmf', 'wfkucx', 'ryedhy', 'qcqfre', 'pdtwdv', 'gdtuna',
#                          'uyugag', 'jimpin', 'gdmigs', 'fetsat', 'kgbeqp', 'vvburq', 'tossxh', 'eqtxhe', 'rzuvuo', 'obtexk', 'fuvnyz', 'znarci', 'zsnuvs',
#                          'ccgtxs', 'rwedna', 'neyepl', 'qqhqwi', 'hkonyw', 'thdmqz', 'qrffuk', 'zoodbw', 'mplaxm', 'evxuce', 'tlvzlx', 'tqksgh', 'nxmrvm',
#                          'przuvuo', 'cicgtxs', 'gulamac', 'jimpyin', 'qqhqwix', 'xadqztq', 'tkossxh', 'zojodbw', 'cizocgw', 'sqzrlhs', 'faepomn', 'tufntzo',
#                          'qroffuk', 'pwcytvt', 'eqtxhre', 'tplvzlx', 'riyedhy', 'obltexk', 'fetsaot', 'wciqoxb', 'pgdmigs', 'tqksugh', 'sluibdm', 'agmyrmf',
#                          'qzsnuvs', 'evxukce', 'wfkuchx', 'neymepl', 'thdmmqz', 'ksszgko', 'taynfxo', 'pqdtwdv', 'qcqfreo', 'rwednad', 'mfttmgv', 'udyugag',
#                          'tmfxxyk', 'znkarci', 'wnyhsmt', 'vhvburq', 'kigbeqp', 'pugzfyk', 'oveyvxl', 'gdtunma', 'gdtunmaw', 'neymepxl', 'xgadqztq', 'grakdthb',
#                          'sluiobdm', 'tkopssxh', 'ouethhse', 'tmfuxxyk', 'ujdyugag', 'kigbkeqp', 'qvroffuk', 'wofkuchx', 'evxuklce', 'mfttmgvj', 'vttpolti',
#                          'qyqhqwix', 'epwcytvt', 'jimpuyin', 'qzsbnuvs', 'przuvuho', 'moydfrwk', 'faepoimn', 'oveyvxfl', 'zohjodbw', 'znkarcii', 'tpufntzo',
#                          'cuicgtxs', 'sqzrlehs', 'hobltexk', 'rwednadd', 'cnnyvmrj', 'qcqfrezo', 'tqksugvh', 'njxkjvmz', 'pougzfyk', 'taplvzlx', 'scizocgw',
#                          'pgdmidgs', 'ksszdgko', 'eqatxhre', 'wqnyhsmt', 'fetosaot', 'ujdyugagn', 'tkaopssxh', 'gdtwunmaw', 'kigbkfeqp', 'wqnyghsmt', 'przuvuhob',
#                          'qyqhjqwix', 'odqphbhkf', 'oeqatxhre', 'cotmfqziz', 'rweydnadd', 'tpaplvzlx', 'faepwoimn', 'tpufntqzo', 'vttpoelti', 'sqzrlehhs', 'vnjxkjvmz',
#                          'moydfrwzk', 'jibmpuyin', 'tmfuxxyku', 'hobxltexk', 'pouegzfyk', 'fetoesaot', 'scinzocgw', 'qzsbnuvsi', 'tqksugvhr', 'neymenpxl', 'jrenjwntk',
#                          'gonpxzngv', 'evrxuklce', 'bwofkuchx', 'zohajodbw', 'pgdmidtgs', 'znkarciui', 'ksszdugko', 'xgadqzptq', 'mftbtmgvj', 'qcqfrezof', 'qvrofgfuk',
#                          'rsgwmsted', 'oveyvxfdl', 'cyuicgtxs', 'cnnyvumrj', 'ouemthhse', 'grakdthtb', 'epwcxytvt', 'kwigbkfeqp', 'tpiufntqzo', 'gmwmzsowjf',
#                          'oeqatxhree', 'epwcjxytvt', 'bwjofkuchx', 'zcmmrtilpt', 'tkaopsssxh', 'vxobwgrdkh', 'faepwobimn', 'ksszdumgko', 'przuvuhobk', 'gcdtwunmaw',
#                          'xmgadqzptq', 'cyuicgtxsu', 'grakdthtbd', 'gznkarciui', 'neymenpxlj', 'qyqhjqwicx', 'jrenjwntkm', 'gonpxzngjv',
#                          'rwkeydnadd', 'qcqfqrezof', 'ouemthhqse', 'qvsrofgfuk', 'cnbnyvumrj', 'odwqphbhkf', 'tqksugvhrc', 'jibmpduyin',
#                          'gsqzrlehhs', 'vnjoxkjvmz', 'pouegnzfyk', 'ujdyujgagn', 'tmfnuxxyku', 'meqczkbnrb', 'moydffrwzk', 'wqnyghnsmt', 'qzsbnuevsi',
#                          'dzohajodbw', 'nvcytywhus', 'ovqeyvxfdl', 'mftbtmgvdj', 'cuotmfqziz', 'tpawplvzlx', 'scinzocgwd', 'pgidmidtgs', 'vttpoeltci',
#                          'evrxukloce', 'kwigbkfeqop', 'rwkedydnadd', 'zcmmrtilpti', 'nvcyutywhus', 'dzohajcodbw', 'tpawplvfzlx', 'grakkdthtbd', 'cnbnyvuhmrj',
#                          'mepjqbuvdku', 'fuaepwobimn', 'meqcfzkbnrb', 'ovqeyvxfdll', 'przujvuhobk', 'tpiuftntqzo', 'cuotmvfqziz', 'uevrxukloce', 'tkqaopsssxh',
#                          'oeqataxhree', 'bwsjofkuchx', 'vzxobwgrdkh', 'gchdtwunmaw', 'odwqphbhkfx', 'yilxbltwwxh', 'gzenkarciui', 'scinzocgwdn', 'axuelrnnwhg',
#                          'qcqfqrezoif', 'qyvsrofgfuk', 'xmgadvqzptq', 'gonpxzvngjv', 'jrenjwntklm', 'gmwamzsowjf', 'ndeymenpxlj', 'moydffrwwzk', 'gsqzrlenhhs',
#                          'qyqhjqweicx', 'qzsbnuejvsi', 'ilojawyersu', 'uesdrhcvbbk', 'cyuicgltxsu', 'ksszdumugko', 'wqnyghnqsmt', 'ujdylujgagn', 'mfftbtmgvdj',
#                          'ikfjaivyrql', 'cuotmvfqzizu', 'vjrenjwntklm', 'uevrxuklobce', 'qyqhjqweizcx', 'oegqataxhree', 'ndeaymenpxlj', 'vodwqphbhkfx', 'gzenkasrciui',
#                          'vzxobwgyrdkh', 'qzwsbnuejvsi', 'qyvsrofgnfuk', 'zcmmrtiklpti', 'wqnlyghnqsmt', 'cyuicgldtxsu', 'ksszdumugiko', 'tpawcplvfzlx', 'axuelrnnnwhg',
#                          'gchdtwwunmaw', 'uiesdrhcvbbk', 'yilxcbltwwxh', 'bwsjofvkuchx', 'mepjqybuvdku', 'przujvuhkobk', 'ujdylujgaagn', 'gmpwamzsowjf', 'tkqaopesssxh',
#                          'ovqeyvxbfdll', 'kwigbkfejqop', 'scinzocgwdwn', 'nvczyutywhus', 'ikfjaivyvrql', 'ilojawyersju', 'moydffrwwyzk', 'grakkbdthtbd', 'uiesdrhcbvbbk',
#                          'kntmjgnqbxlwh', 'ikfjaivyvreql', 'wqnlyghnqsmtt', 'kewigbkfejqop', 'moyddffrwwyzk', 'kutkavldvvqvp', 'vjrenjwntklqm', 'vodwqpzhbhkfx',
#                          'vzxobwgyhrdkh', 'gchdtwgwunmaw', 'ytpawcplvfzlx', 'qbzwsbnuejvsi', 'bwsjofvkupchx', 'przujvuxhkobk', 'ovqeyvxubfdll', 'nvczwyutywhus',
#                          'qyqhjqwegizcx', 'cuotmvfqzinzu', 'zcmmrtsiklpti', 'ksyszdumugiko', 'ndzeaymenpxlj', 'uevirxuklobce', 'cyuicgldtxwsu', 'scinzocgwdwhn',
#                          'iaxuelrnnnwhg', 'ujadylujgaagn', 'uqyqhjqwegizcx', 'kewiygbkfejqop', 'vzxiobwgyhrdkh', 'cyuicglbdtxwsu', 'bwsjofvkuptchx', 'zscinzocgwdwhn',
#                          'vodwqpzhbhjkfx', 'przujvuaxhkobk', 'wqnlyguhnqsmtt', 'kntmmjgnqbxlwh', 'ndzeaylmenpxlj', 'moyddffrhwwyzk', 'qbzwsbnuejvsoi', 'cuotmvfqziknzu',
#                          'uiesdrhcbvobbk', 'ovqheyvxubfdll', 'ujadylujgaagsn', 'ytpawcplvifzlx', 'nvcyzwyutywhus', 'zcmmrtsitklpti', 'kntmmjgnqbxtlwh',
#                          'uqyqhjqdwegizcx', 'cusotmvfqziknzu', 'kewiylgbkfejqop', 'zscinzobcgwdwhn', 'nvcxyzwyutywhus', 'qbzwsbnuejvsmoi', 'moyddffrhwwyezk',
#                          'bdwwnalubvxtdgu', 'ovqheyvxubfdtll', 'cyquicglbdtxwsu', 'bwsjofvkmuptchx', 'uiesdrehcbvobbk', 'veodwqpzhbhjkfx', 'ujadylujgaazgsn',
#                          'prpzujvuaxhkobk', 'ndzeaylmetnpxlj', 'blmwegckaplwjpo', 'blmwegckaplqwjpo', 'ndozeaylmetnpxlj', 'bdwwnalubrvxtdgu', 'zscinzobcgtwdwhn',
#                          'prpzuujvuaxhkobk', 'ujhadylujgaazgsn', 'qbzwsbnuejvsmvoi', 'uqqyqhjqdwegizcx', 'bwsjofvkmuptchxy', 'nvcxyzwyutywhuhs', 'cusotmvfqzwiknzu',
#                          'ovqheyvxubsfdtll', 'kntmmjognqbxtlwh', 'kewiylgbkfejqfop']))
