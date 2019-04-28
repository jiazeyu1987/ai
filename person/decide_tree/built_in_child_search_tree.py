from jtree import *
from person import *



def init_base_search_tree_child(self):
    strlist = [PerceptionSee.unique_flag(), ActionWatching.unique_flag()]
    jtree_chain = JTreeChain()
    jtree_chain.create_chain_by_strlist(strlist)
    self.search_tree.add_chain(jtree_chain)


    strlist = [PerceptionHunger.unique_flag(), ActionCry.unique_flag()]
    jtree_chain = JTreeChain()
    jtree_chain.create_chain_by_strlist(strlist)
    self.search_tree.add_chain(jtree_chain)

    strlist = [PerceptionWannaPlay.unique_flag(), ActionPlay.unique_flag()]
    jtree_chain = JTreeChain()
    jtree_chain.create_chain_by_strlist(strlist)
    self.search_tree.add_chain(jtree_chain)

    strlist = ActionPlay.create()
    jtree_chain = JTreeChain()
    jtree_chain.create_chain_by_strlist(strlist)
    self.search_tree.add_chain(jtree_chain)

    strlist = ActionCry.create()
    jtree_chain = JTreeChain()
    jtree_chain.create_chain_by_strlist(strlist)
    self.search_tree.add_chain(jtree_chain)

    strlist = ActionWatching.create()
    jtree_chain = JTreeChain()
    jtree_chain.create_chain_by_strlist(strlist)
    self.search_tree.add_chain(jtree_chain)