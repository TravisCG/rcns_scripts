#!/bin/bash
# cat files | nl -v 2 -w 3 -n rz | awk '{print "scp ~/.ssh/id_rsa dev-genom-worker"$1":.ssh/\nscp prepare.sh runner.sh dev-genom-worker"$1":\nssh dev-genom-worker"$1" '\''./runner.sh "$2" >log.txt 2>err.txt'\''"}'
# move the scripts to the worker nodes and run them
scp ~/.ssh/id_rsa dev-genom-worker002:.ssh/
scp prepare.sh runner.sh dev-genom-worker002:
ssh dev-genom-worker002 './runner.sh D0111408 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker003:.ssh/
scp prepare.sh runner.sh dev-genom-worker003:
ssh dev-genom-worker003 './runner.sh D0211409 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker004:.ssh/
scp prepare.sh runner.sh dev-genom-worker004:
ssh dev-genom-worker004 './runner.sh D0311410 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker005:.ssh/
scp prepare.sh runner.sh dev-genom-worker005:
ssh dev-genom-worker005 './runner.sh D0411411 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker006:.ssh/
scp prepare.sh runner.sh dev-genom-worker006:
ssh dev-genom-worker006 './runner.sh D0511412 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker007:.ssh/
scp prepare.sh runner.sh dev-genom-worker007:
ssh dev-genom-worker007 './runner.sh D0611413 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker008:.ssh/
scp prepare.sh runner.sh dev-genom-worker008:
ssh dev-genom-worker008 './runner.sh D0711414 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker009:.ssh/
scp prepare.sh runner.sh dev-genom-worker009:
ssh dev-genom-worker009 './runner.sh D0811415 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker010:.ssh/
scp prepare.sh runner.sh dev-genom-worker010:
ssh dev-genom-worker010 './runner.sh D0911416 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker011:.ssh/
scp prepare.sh runner.sh dev-genom-worker011:
ssh dev-genom-worker011 './runner.sh D1011417 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker012:.ssh/
scp prepare.sh runner.sh dev-genom-worker012:
ssh dev-genom-worker012 './runner.sh D1111046 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker013:.ssh/
scp prepare.sh runner.sh dev-genom-worker013:
ssh dev-genom-worker013 './runner.sh D1211052 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker014:.ssh/
scp prepare.sh runner.sh dev-genom-worker014:
ssh dev-genom-worker014 './runner.sh D1311054 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker015:.ssh/
scp prepare.sh runner.sh dev-genom-worker015:
ssh dev-genom-worker015 './runner.sh D1411055 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker016:.ssh/
scp prepare.sh runner.sh dev-genom-worker016:
ssh dev-genom-worker016 './runner.sh D1511053 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker017:.ssh/
scp prepare.sh runner.sh dev-genom-worker017:
ssh dev-genom-worker017 './runner.sh D4415274 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker018:.ssh/
scp prepare.sh runner.sh dev-genom-worker018:
ssh dev-genom-worker018 './runner.sh D4515275 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker019:.ssh/
scp prepare.sh runner.sh dev-genom-worker019:
ssh dev-genom-worker019 './runner.sh D4615276 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker020:.ssh/
scp prepare.sh runner.sh dev-genom-worker020:
ssh dev-genom-worker020 './runner.sh D4715277 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker021:.ssh/
scp prepare.sh runner.sh dev-genom-worker021:
ssh dev-genom-worker021 './runner.sh H_59 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker022:.ssh/
scp prepare.sh runner.sh dev-genom-worker022:
ssh dev-genom-worker022 './runner.sh H_60 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker023:.ssh/
scp prepare.sh runner.sh dev-genom-worker023:
ssh dev-genom-worker023 './runner.sh H_62 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker024:.ssh/
scp prepare.sh runner.sh dev-genom-worker024:
ssh dev-genom-worker024 './runner.sh H_64 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker025:.ssh/
scp prepare.sh runner.sh dev-genom-worker025:
ssh dev-genom-worker025 './runner.sh H_65 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker026:.ssh/
scp prepare.sh runner.sh dev-genom-worker026:
ssh dev-genom-worker026 './runner.sh H_66 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker027:.ssh/
scp prepare.sh runner.sh dev-genom-worker027:
ssh dev-genom-worker027 './runner.sh H_67 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker028:.ssh/
scp prepare.sh runner.sh dev-genom-worker028:
ssh dev-genom-worker028 './runner.sh H_68 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker029:.ssh/
scp prepare.sh runner.sh dev-genom-worker029:
ssh dev-genom-worker029 './runner.sh H_70 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker030:.ssh/
scp prepare.sh runner.sh dev-genom-worker030:
ssh dev-genom-worker030 './runner.sh H_71 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker031:.ssh/
scp prepare.sh runner.sh dev-genom-worker031:
ssh dev-genom-worker031 './runner.sh H_72 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker032:.ssh/
scp prepare.sh runner.sh dev-genom-worker032:
ssh dev-genom-worker032 './runner.sh H_73 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker033:.ssh/
scp prepare.sh runner.sh dev-genom-worker033:
ssh dev-genom-worker033 './runner.sh H_74 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker034:.ssh/
scp prepare.sh runner.sh dev-genom-worker034:
ssh dev-genom-worker034 './runner.sh mbk_41 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker035:.ssh/
scp prepare.sh runner.sh dev-genom-worker035:
ssh dev-genom-worker035 './runner.sh mbk_42 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker036:.ssh/
scp prepare.sh runner.sh dev-genom-worker036:
ssh dev-genom-worker036 './runner.sh mbk_43 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker037:.ssh/
scp prepare.sh runner.sh dev-genom-worker037:
ssh dev-genom-worker037 './runner.sh mbk_44 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker038:.ssh/
scp prepare.sh runner.sh dev-genom-worker038:
ssh dev-genom-worker038 './runner.sh mbk_45 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker039:.ssh/
scp prepare.sh runner.sh dev-genom-worker039:
ssh dev-genom-worker039 './runner.sh mbk_46 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker040:.ssh/
scp prepare.sh runner.sh dev-genom-worker040:
ssh dev-genom-worker040 './runner.sh mbk_47 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker041:.ssh/
scp prepare.sh runner.sh dev-genom-worker041:
ssh dev-genom-worker041 './runner.sh mbk_48 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker042:.ssh/
scp prepare.sh runner.sh dev-genom-worker042:
ssh dev-genom-worker042 './runner.sh mbk_49 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker043:.ssh/
scp prepare.sh runner.sh dev-genom-worker043:
ssh dev-genom-worker043 './runner.sh mbk_50 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker044:.ssh/
scp prepare.sh runner.sh dev-genom-worker044:
ssh dev-genom-worker044 './runner.sh mbk_51 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker045:.ssh/
scp prepare.sh runner.sh dev-genom-worker045:
ssh dev-genom-worker045 './runner.sh mbk_52 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker046:.ssh/
scp prepare.sh runner.sh dev-genom-worker046:
ssh dev-genom-worker046 './runner.sh mbk_53 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker047:.ssh/
scp prepare.sh runner.sh dev-genom-worker047:
ssh dev-genom-worker047 './runner.sh mbk_54 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker048:.ssh/
scp prepare.sh runner.sh dev-genom-worker048:
ssh dev-genom-worker048 './runner.sh mbk_55 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker049:.ssh/
scp prepare.sh runner.sh dev-genom-worker049:
ssh dev-genom-worker049 './runner.sh mbk_56 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker050:.ssh/
scp prepare.sh runner.sh dev-genom-worker050:
ssh dev-genom-worker050 './runner.sh mbk_65 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker051:.ssh/
scp prepare.sh runner.sh dev-genom-worker051:
ssh dev-genom-worker051 './runner.sh mbk_66 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker052:.ssh/
scp prepare.sh runner.sh dev-genom-worker052:
ssh dev-genom-worker052 './runner.sh mbk_67 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker053:.ssh/
scp prepare.sh runner.sh dev-genom-worker053:
ssh dev-genom-worker053 './runner.sh mbk_68 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker054:.ssh/
scp prepare.sh runner.sh dev-genom-worker054:
ssh dev-genom-worker054 './runner.sh mbk_69 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker055:.ssh/
scp prepare.sh runner.sh dev-genom-worker055:
ssh dev-genom-worker055 './runner.sh mbk_70 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker056:.ssh/
scp prepare.sh runner.sh dev-genom-worker056:
ssh dev-genom-worker056 './runner.sh mbk_71 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker057:.ssh/
scp prepare.sh runner.sh dev-genom-worker057:
ssh dev-genom-worker057 './runner.sh R0118712 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker058:.ssh/
scp prepare.sh runner.sh dev-genom-worker058:
ssh dev-genom-worker058 './runner.sh R0218713 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker059:.ssh/
scp prepare.sh runner.sh dev-genom-worker059:
ssh dev-genom-worker059 './runner.sh R0318714 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker060:.ssh/
scp prepare.sh runner.sh dev-genom-worker060:
ssh dev-genom-worker060 './runner.sh R0418715 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker061:.ssh/
scp prepare.sh runner.sh dev-genom-worker061:
ssh dev-genom-worker061 './runner.sh R0518688 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker062:.ssh/
scp prepare.sh runner.sh dev-genom-worker062:
ssh dev-genom-worker062 './runner.sh R0518716 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker063:.ssh/
scp prepare.sh runner.sh dev-genom-worker063:
ssh dev-genom-worker063 './runner.sh R0618717 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker064:.ssh/
scp prepare.sh runner.sh dev-genom-worker064:
ssh dev-genom-worker064 './runner.sh R0618927 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker065:.ssh/
scp prepare.sh runner.sh dev-genom-worker065:
ssh dev-genom-worker065 './runner.sh R0718711 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker066:.ssh/
scp prepare.sh runner.sh dev-genom-worker066:
ssh dev-genom-worker066 './runner.sh R0718718 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker067:.ssh/
scp prepare.sh runner.sh dev-genom-worker067:
ssh dev-genom-worker067 './runner.sh R0818719 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker068:.ssh/
scp prepare.sh runner.sh dev-genom-worker068:
ssh dev-genom-worker068 './runner.sh R0818926 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker069:.ssh/
scp prepare.sh runner.sh dev-genom-worker069:
ssh dev-genom-worker069 './runner.sh R0918720 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker070:.ssh/
scp prepare.sh runner.sh dev-genom-worker070:
ssh dev-genom-worker070 './runner.sh R1018721 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker071:.ssh/
scp prepare.sh runner.sh dev-genom-worker071:
ssh dev-genom-worker071 './runner.sh R1118722 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker072:.ssh/
scp prepare.sh runner.sh dev-genom-worker072:
ssh dev-genom-worker072 './runner.sh R1218723 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker073:.ssh/
scp prepare.sh runner.sh dev-genom-worker073:
ssh dev-genom-worker073 './runner.sh R1318724 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker074:.ssh/
scp prepare.sh runner.sh dev-genom-worker074:
ssh dev-genom-worker074 './runner.sh R1418725 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker075:.ssh/
scp prepare.sh runner.sh dev-genom-worker075:
ssh dev-genom-worker075 './runner.sh R1518726 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker076:.ssh/
scp prepare.sh runner.sh dev-genom-worker076:
ssh dev-genom-worker076 './runner.sh R1618727 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker077:.ssh/
scp prepare.sh runner.sh dev-genom-worker077:
ssh dev-genom-worker077 './runner.sh R1718728 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker078:.ssh/
scp prepare.sh runner.sh dev-genom-worker078:
ssh dev-genom-worker078 './runner.sh R1818729 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker079:.ssh/
scp prepare.sh runner.sh dev-genom-worker079:
ssh dev-genom-worker079 './runner.sh R1919002 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker080:.ssh/
scp prepare.sh runner.sh dev-genom-worker080:
ssh dev-genom-worker080 './runner.sh R2019003 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker081:.ssh/
scp prepare.sh runner.sh dev-genom-worker081:
ssh dev-genom-worker081 './runner.sh R2119004 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker082:.ssh/
scp prepare.sh runner.sh dev-genom-worker082:
ssh dev-genom-worker082 './runner.sh R2219005 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker083:.ssh/
scp prepare.sh runner.sh dev-genom-worker083:
ssh dev-genom-worker083 './runner.sh R2319006 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker084:.ssh/
scp prepare.sh runner.sh dev-genom-worker084:
ssh dev-genom-worker084 './runner.sh R2419007 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker085:.ssh/
scp prepare.sh runner.sh dev-genom-worker085:
ssh dev-genom-worker085 './runner.sh R2519008 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker086:.ssh/
scp prepare.sh runner.sh dev-genom-worker086:
ssh dev-genom-worker086 './runner.sh R2619009 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker087:.ssh/
scp prepare.sh runner.sh dev-genom-worker087:
ssh dev-genom-worker087 './runner.sh R2719010 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker088:.ssh/
scp prepare.sh runner.sh dev-genom-worker088:
ssh dev-genom-worker088 './runner.sh R2819011 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker089:.ssh/
scp prepare.sh runner.sh dev-genom-worker089:
ssh dev-genom-worker089 './runner.sh R2919012 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker090:.ssh/
scp prepare.sh runner.sh dev-genom-worker090:
ssh dev-genom-worker090 './runner.sh R3019013 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker091:.ssh/
scp prepare.sh runner.sh dev-genom-worker091:
ssh dev-genom-worker091 './runner.sh R3119014 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker092:.ssh/
scp prepare.sh runner.sh dev-genom-worker092:
ssh dev-genom-worker092 './runner.sh R3219015 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker093:.ssh/
scp prepare.sh runner.sh dev-genom-worker093:
ssh dev-genom-worker093 './runner.sh R3319016 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker094:.ssh/
scp prepare.sh runner.sh dev-genom-worker094:
ssh dev-genom-worker094 './runner.sh R3419017 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker095:.ssh/
scp prepare.sh runner.sh dev-genom-worker095:
ssh dev-genom-worker095 './runner.sh R3519018 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker096:.ssh/
scp prepare.sh runner.sh dev-genom-worker096:
ssh dev-genom-worker096 './runner.sh R3619019 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker097:.ssh/
scp prepare.sh runner.sh dev-genom-worker097:
ssh dev-genom-worker097 './runner.sh R3719020 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker098:.ssh/
scp prepare.sh runner.sh dev-genom-worker098:
ssh dev-genom-worker098 './runner.sh R3819021 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker099:.ssh/
scp prepare.sh runner.sh dev-genom-worker099:
ssh dev-genom-worker099 './runner.sh S0118783 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker100:.ssh/
scp prepare.sh runner.sh dev-genom-worker100:
ssh dev-genom-worker100 './runner.sh S0218807 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker101:.ssh/
scp prepare.sh runner.sh dev-genom-worker101:
ssh dev-genom-worker101 './runner.sh S0318778 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker102:.ssh/
scp prepare.sh runner.sh dev-genom-worker102:
ssh dev-genom-worker102 './runner.sh S0418798 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker103:.ssh/
scp prepare.sh runner.sh dev-genom-worker103:
ssh dev-genom-worker103 './runner.sh S3918778 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker104:.ssh/
scp prepare.sh runner.sh dev-genom-worker104:
ssh dev-genom-worker104 './runner.sh S4018798 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker105:.ssh/
scp prepare.sh runner.sh dev-genom-worker105:
ssh dev-genom-worker105 './runner.sh S4118807 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker106:.ssh/
scp prepare.sh runner.sh dev-genom-worker106:
ssh dev-genom-worker106 './runner.sh S4218803 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker107:.ssh/
scp prepare.sh runner.sh dev-genom-worker107:
ssh dev-genom-worker107 './runner.sh S4318797 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker108:.ssh/
scp prepare.sh runner.sh dev-genom-worker108:
ssh dev-genom-worker108 './runner.sh S4418783 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker109:.ssh/
scp prepare.sh runner.sh dev-genom-worker109:
ssh dev-genom-worker109 './runner.sh S4518805 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker110:.ssh/
scp prepare.sh runner.sh dev-genom-worker110:
ssh dev-genom-worker110 './runner.sh S4618810 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker111:.ssh/
scp prepare.sh runner.sh dev-genom-worker111:
ssh dev-genom-worker111 './runner.sh S4718794 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker112:.ssh/
scp prepare.sh runner.sh dev-genom-worker112:
ssh dev-genom-worker112 './runner.sh S4818978 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker113:.ssh/
scp prepare.sh runner.sh dev-genom-worker113:
ssh dev-genom-worker113 './runner.sh S4918980 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker114:.ssh/
scp prepare.sh runner.sh dev-genom-worker114:
ssh dev-genom-worker114 './runner.sh S5018963 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker115:.ssh/
scp prepare.sh runner.sh dev-genom-worker115:
ssh dev-genom-worker115 './runner.sh S5118942 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker116:.ssh/
scp prepare.sh runner.sh dev-genom-worker116:
ssh dev-genom-worker116 './runner.sh S5318977 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker117:.ssh/
scp prepare.sh runner.sh dev-genom-worker117:
ssh dev-genom-worker117 './runner.sh S5518957 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker118:.ssh/
scp prepare.sh runner.sh dev-genom-worker118:
ssh dev-genom-worker118 './runner.sh S5818959 >log.txt 2>err.txt'
scp ~/.ssh/id_rsa dev-genom-worker119:.ssh/
scp prepare.sh runner.sh dev-genom-worker119:
ssh dev-genom-worker119 './runner.sh S6018967 >log.txt 2>err.txt'
