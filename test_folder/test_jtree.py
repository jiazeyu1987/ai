from jtree import *
def test_jtree1():
    jtree_main = JTreeMain()

    strlist = ["1","2","3","4","5","6","7"]
    jtree_chain = JTreeChain()
    jtree_chain.create_chain_by_strlist(strlist)
    jtree_main.add("1",jtree_chain)

    strlist = ["1", "2", "31", "4", "5", "6", "7"]
    jtree_chain = JTreeChain()
    jtree_chain.create_chain_by_strlist(strlist)
    jtree_main.add("1", jtree_chain)
    strlist = ["1", "2", "31", "41", "5", "6", "7"]
    jtree_chain = JTreeChain()
    jtree_chain.create_chain_by_strlist(strlist)
    jtree_main.add("1", jtree_chain)

    strlist = ["1", "2", "3", "41", "5", "6", "7"]
    jtree_chain = JTreeChain()
    jtree_chain.create_chain_by_strlist(strlist)
    jtree_main.add("1", jtree_chain)

    strlist = ["1", "2", "3", "41", "5", "6", "711"]
    jtree_chain = JTreeChain()
    jtree_chain.create_chain_by_strlist(strlist)
    jtree_main.add("1", jtree_chain)

    jtree_chain = jtree_main.find("1")
    print(jtree_chain)

