import time

from django.shortcuts import render
from django.http import HttpResponse
import requests


def home(request):
    class Account:
        account = None
        balance = None

        def __init__(self, account):
            self.account = account

    accounts = []
    accounts.append(Account('0x00000000219ab540356cbb839cbe05303d7705fa'))
    accounts.append(Account('0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'))
    accounts.append(Account('0xDA9dfA130Df4dE4673b89022EE50ff26f6EA73Cf'))
    accounts.append(Account('0x73BCEb1Cd57C711feaC4224D062b0F6ff338501e'))
    accounts.append(Account('0xBE0eB53F46cd790Cd13851d5EFf43D12404d33E8'))
    accounts.append(Account('0x9BF4001d307dFd62B26A2F1307ee0C0307632d59'))
    accounts.append(Account('0x4Ddc2D193948926D02f9B1fE9e1daa0718270ED5'))
    accounts.append(Account('0x61EDCDf5bb737ADffE5043706e7C5bb1f1a56eEA'))
    accounts.append(Account('0xDC24316b9AE028F1497c275EB9192a3Ea0f67022'))
    accounts.append(Account('0x1b3cB81E51011b549d78bf720b0d924ac763A7C2'))

    accounts.append(Account('0x011b6e24ffb0b5f5fcc564cf4183c5bbbc96d515'))
    accounts.append(Account('0x8484ef722627bf18ca5ae6bcf031c23e6e922b30'))
    accounts.append(Account('0x07ee55aa48bb72dcc6e9d78256648910de513eca'))
    accounts.append(Account('0xc61b9bb3a7a0767e3179713f3a5c7a9aedce193c'))
    accounts.append(Account('0xe92d1a43df510f82c66382592a047d288f85226f'))
    accounts.append(Account('0xf977814e90da44bfa03b6295a0616a897441acec'))
    accounts.append(Account('0x742d35cc6634c0532925a3b844bc454e4438f44e'))
    accounts.append(Account('0xdf9eb223bafbe5c5271415c75aecd68c21fe3d7f'))
    accounts.append(Account('0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae'))
    accounts.append(Account('0xa929022c9107643515f5c777ce9a910f0d1e490c'))

    accounts.append(Account('0x220866b1a2219f40e72f5c628b65d54268ca3a9d'))
    accounts.append(Account('0xca8fa8f0b631ecdb18cda619c4fc9d197c8affca'))
    accounts.append(Account('0x176f3dab24a159341c0509bb36b833e7fdd0a132'))
    accounts.append(Account('0x3bfc20f0b9afcace800d73d2191166ff16540258'))
    accounts.append(Account('0x6262998ced04146fa42253a5c0af90ca02dfd2a3'))
    accounts.append(Account('0x8103683202aa8da10536036edef04cdd865c225e'))
    accounts.append(Account('0xa7efae728d2936e78bda97dc267687568dd593f3'))
    accounts.append(Account('0x0a4c79ce84202b03e95b7a692e5d728d83c44c76'))
    accounts.append(Account('0x7d24796f7ddb17d73e8b1d0a3bbd103fba2cb2fe'))
    accounts.append(Account('0x2b6ed29a95753c3ad948348e3e7b1a251080ffb9'))

    accounts.append(Account('0xbddf00563c9abd25b576017f08c46982012f12be'))
    accounts.append(Account('0x189b9cbd4aff470af2c0102f365fc1823d857965'))
    accounts.append(Account('0x9845e1909dca337944a0272f1f9f7249833d2d19'))
    accounts.append(Account('0x0548f59fee79f8832c299e01dca5c76f034f558e'))
    accounts.append(Account('0x59448fe20378357f206880c58068f095ae63d5a5'))
    accounts.append(Account('0x0c23fc0ef06716d2f8ba19bc4bed56d045581f2d'))
    accounts.append(Account('0x2faf487a4414fe77e2327f0bf4ae2a264a776ad2'))
    accounts.append(Account('0x66f820a414680b5bcda5eeca5dea238543f42054'))
    accounts.append(Account('0xb29380ffc20696729b7ab8d093fa1e2ec14dfe2b'))
    accounts.append(Account('0x558553d54183a8542f7832742e7b4ba9c33aa1e6'))

    accounts.append(Account('0x98ec059dc3adfbdd63429454aeb0c990fba4a128'))
    accounts.append(Account('0xcdbf58a9a9b54a2c43800c50c7192946de858321'))
    accounts.append(Account('0x19184ab45c40c2920b0e0e31413b9434abd243ed'))
    accounts.append(Account('0x90a9e09501b70570f9b11df2a6d4f047f8630d6d'))
    accounts.append(Account('0xbf3aeb96e164ae67e763d9e050ff124e7c3fdd28'))
    accounts.append(Account('0xb8808f9e9b88497ec522304055cd537a0913f6a0'))
    accounts.append(Account('0xf774da4418c6dca3051f0e7570829b24214e730b'))
    accounts.append(Account('0x1db92e2eebc8e0c075a02bea49a2935bcd2dfcf4'))
    accounts.append(Account('0xdc1487e092caba080c6badafaa75a58ce7a2ec34'))
    accounts.append(Account('0x36a85757645e8e8aec062a1dee289c7d615901ca'))

    accounts.append(Account('0xd69b0089d9ca950640f5dc9931a41a5965f00303'))
    accounts.append(Account('0xa7e4fecddc20d83f36971b67e13f1abc98dfcfa6'))
    accounts.append(Account('0x7da82c7ab4771ff031b66538d2fb9b0b047f6cf9'))
    accounts.append(Account('0x5b5b69f4e0add2df5d2176d7dbd20b4897bc7ec4'))
    accounts.append(Account('0x78605df79524164911c144801f41e9811b7db73d'))
    accounts.append(Account('0x3ba25081d3935fcc6788e6220abcace39d58d95d'))
    accounts.append(Account('0xef22c14f46858d5ac61326497b056974167f2ee1'))
    accounts.append(Account('0xfd898a0f677e97a9031654fc79a27cb5e31da34a'))
    accounts.append(Account('0x701c484bfb40ac628afa487b6082f084b14af0bd'))
    accounts.append(Account('0x4b4a011c420b91260a272afd91e54accdafdfc1d'))

    accounts.append(Account('0xa8dcc0373822b94d7f57326be24ca67bafcaad6b'))
    accounts.append(Account('0x367989c660881e1ca693730f7126fe0ffc0963fb'))
    accounts.append(Account('0x0ff64c53d295533a37f913bb78be9e2adc78f5fe'))
    accounts.append(Account('0x844ada2ed8ecd77a1a9c72912df0fcb8b8c495a7'))
    accounts.append(Account('0x9c2fc4fc75fa2d7eb5ba9147fa7430756654faa9'))
    accounts.append(Account('0xb20411c403687d1036e05c8a7310a0f218429503'))
    accounts.append(Account('0x9a1ed80ebc9936cee2d3db944ee6bd8d407e7f9f'))
    accounts.append(Account('0xb8cda067fabedd1bb6c11c626862d7255a2414fe'))
    accounts.append(Account('0xb9fa6e54025b4f0829d8e1b42e8b846914659632'))
    accounts.append(Account('0xba18ded5e0d604a86428282964ae0bb249ceb9d0'))

    accounts.append(Account('0xfe01a216234f79cfc3bea7513e457c6a9e50250d'))
    accounts.append(Account('0x0c05ec4db907cfb91b2a1a29e7b86688b7568a6d'))
    accounts.append(Account('0xc4cf565a5d25ee2803c9b8e91fc3d7c62e79fe69'))
    accounts.append(Account('0xe04cf52e9fafa3d9bf14c407afff94165ef835f7'))
    accounts.append(Account('0x77afe94859163abf0b90725d69e904ea91446c7b'))
    accounts.append(Account('0x19d599012788b991ff542f31208bab21ea38403e'))
    accounts.append(Account('0xca582d9655a50e6512045740deb0de3a7ee5281f'))
    accounts.append(Account('0xd05e6bf1a00b5b4c9df909309f19e29af792422b'))
    accounts.append(Account('0x0f00294c6e4c30d9ffc0557fec6c586e6f8c3935'))
    accounts.append(Account('0xeb2b00042ce4522ce2d1aacee6f312d26c4eb9d6'))

    accounts.append(Account('0x7ae92148e79d60a0749fd6de374c8e81dfddf792'))
    accounts.append(Account('0x554f4476825293d4ad20e02b54aca13956acc40a'))
    accounts.append(Account('0x9cf36e93a8e2b1eaaa779d9965f46c90b820048c'))
    accounts.append(Account('0x4756eeebf378046f8dd3cb6fa908d93bfd45f139'))
    accounts.append(Account('0x091933ee1088cdf5daace8baec0997a4e93f0dd6'))
    accounts.append(Account('0xa0efb63be0db8fc11681a598bf351a42a6ff50e0'))
    accounts.append(Account('0x8b83b9c4683aa4ec897c569010f09c6d04608163'))
    accounts.append(Account('0x550cd530bc893fc6d2b4df6bea587f17142ab64e'))
    accounts.append(Account('0x828103b231b39fffce028562412b3c04a4640e64'))
    accounts.append(Account('0xe35b0ef92452c353dbb93775e0df97cedf873c72'))

    accounts.append(Account('0x0518f5bb058f6215a0ff5f4df54dae832d734e04'))
    accounts.append(Account('0x0e86733eab26cfcc04bb1752a62ec88e910b4cf5'))
    accounts.append(Account('0xb8b6fe7f357adeab950ac6c270ce340a46989ce1'))
    accounts.append(Account('0xeddf8eb4984cc27407a568cae1c78a1ddb0c2c1b'))
    accounts.append(Account('0x7145cfedcf479bede20c0a4ba1868c93507d5786'))
    accounts.append(Account('0x2fa9f9efc767650aace0422668444c3ff63e1f8d'))
    accounts.append(Account('0xa160cdab225685da1d56aa342ad8841c3b53f291'))
    accounts.append(Account('0xd57479b8287666b44978255f1677e412d454d4f0'))
    accounts.append(Account('0x4baf012726cb5ec7dda57bc2770798a38100c44d'))
    accounts.append(Account('0x67fde691b11e96083fc52a5b74d73f0695811a3b'))


    cnt = 0
    for i in accounts:
        cnt += 1
        if cnt == 5:
            time.sleep(1)
            cnt = 0

        a = eval(requests.get('https://api.etherscan.io/api?module=account&action=balance&address='+i.account+'&tag=latest&apikey=E7AN71NS1A2I6IQ387AIQERFPAYAHQQXBA').text)
        i.balance = int(a['result']) / 1000000000000000000

    return render(request, 'index.html', {'accounts': accounts})
