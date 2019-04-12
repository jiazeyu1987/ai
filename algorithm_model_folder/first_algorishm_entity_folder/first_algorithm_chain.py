from .first_algorithm_chain_node import FirstAlgorithmChainNode
import utils
class FirstAlgorithmChain:
    def __init__(self):
        self._chain = None
        self._temp_chain = None
        self._qualify_list_datas = []
        self._unqualify_list_datas = []
        self._unhandle_nodes = []
        self._chain_pool = []
        self.rate = 0
    def __str__(self):
        self._chain.print_chain()
        print("================================")
        print("rate:"+str(self.rate))
        print("qulify data list")
        for k in self._qualify_list_datas:
            print(k)
        print("unqulify data list")
        for k in self._unqualify_list_datas:
            print(k)
        return ""

    def add_entity_list(self,list1):
        pre_node = None
        for i in range(len(list1._list)):
            entity = list1._list[i]
            node = None
            if entity.is_known():
                node = FirstAlgorithmChainNode("normal")
                node.add_value(entity.get_value())
                pass
            else:
                node = FirstAlgorithmChainNode("fake")
                node.add_value(entity.get_value())
            if(pre_node==None):
                pre_node = node
            else:
                pre_node.set_next(node)
                pre_node = node
        #pre_node.print_chain()
        first_node = pre_node.find_first_node()
        self._unhandle_nodes.append(first_node)



    def merge_chains(self,origin_data):
        #print(len(self._unhandle_nodes))

        for i in range(len(self._unhandle_nodes)):
            unfit = 0
            self._temp_chain = self._unhandle_nodes[i]
            if (self._temp_chain != None):
                for k in range(len(origin_data)):
                    if (self._is_origin_data_fit_chain(origin_data[k])):
                        pass
                    else:
                        unfit += 1
                self._chain_pool.append((unfit, -len(self._get_normal_nodes()), self._temp_chain))

        # for i in range(len(self._unhandle_nodes)):
        #     for j in range(len(self._unhandle_nodes)):
        #         if(i<j):
        #             self._merge_2_chain(self._unhandle_nodes[i],self._unhandle_nodes[j])
        #             #self._temp_chain.print_chain(1)
        #             unfit=0
        #             if(self._temp_chain!=None):
        #                 for k in range(len(origin_data)):
        #                     if (self._is_origin_data_fit_chain(origin_data[k])):
        #                         pass
        #                     else:
        #                         unfit+=1
        #                 self._chain_pool.append((unfit,-len(self._get_normal_nodes()),self._temp_chain))



        self._chain_pool = sorted(self._chain_pool,key=lambda pair:(pair[0],pair[1]))

        new_pool = []
        for i in range(len(self._chain_pool)):
            if self._chain_pool[i][1]<0:
                new_pool.append(self._chain_pool[i])
        self._chain_pool = new_pool



        if(len(self._chain_pool)<1):
            raise Exception('sldfjalsdkfjas;dfk')
        tmp_chain = self._chain_pool[0]
        if(tmp_chain[0]!=0 ):
            len1 = len(origin_data)
            self.rate = (int)(100*(len1-tmp_chain[0])/len1)
        else:
            self.rate = 100
        new_chain = tmp_chain[2]
        self._create_exact_chain(new_chain,origin_data)
        #new_chain.print_chain()

    # def _create_exact_chain(self,new_chain,origin_data):
    #     for i in range(len(origin_data)):
    #         self._create_exact_chain_list(new_chain,origin_data[i])
    def _create_exact_chain(self,new_chain,origin_data):
        source = new_chain.find_first_node()
        last_index=[]
        exact_node = None
        for i in range(len(origin_data)):
            last_index.append(0)
        while (source != None):
            while (source != None and source.get_type() != "normal"):
                source = source.next()
            if (source == None):
                break
            switch_node = FirstAlgorithmChainNode("switch")
            for i in range(len(origin_data)):
                ori = origin_data[i]

                marks,unmarks = utils.get_marks(origin_data[i],source.get_value())
                if (len(marks)) == 0:
                    if(ori in self._unqualify_list_datas):
                        pass
                    else:
                        self._unqualify_list_datas.append(ori)
                    continue
                else:
                    flag = False
                    for key2 in range(len(marks)):
                        key1 = marks[key2]
                        if key1[0] < last_index[i]:
                            pass
                        else:
                            if(last_index[i]<key1[0]):
                                sublist = origin_data[i][last_index[i]:key1[0]]
                                switch_node.add_nodes(sublist)
                            last_index[i] = key1[0] + key1[1]
                            flag = True
                            break
                    if (flag == False):
                        raise Exception("sldkjfalskdfja;sdkfj")
            sc = source.clone()
            if(exact_node!=None):
                if(switch_node.nodes_number()>0):
                    exact_node.set_next(switch_node)
                    switch_node.set_next(sc)
                else:
                    exact_node.set_next(sc)
                exact_node = sc
            else:
                if (switch_node.nodes_number() > 0):
                    exact_node = (switch_node)
                    switch_node.set_next(sc)
                else:
                    exact_node = sc
                exact_node = sc
            source = source.next()

        switch_node = FirstAlgorithmChainNode("switch")
        for i in range(len(origin_data)):
            if(last_index[i]<len(origin_data[i]) and (origin_data[i] in self._unqualify_list_datas)==False):
                val = origin_data[i][last_index[i]:len(origin_data[i])]
                switch_node.add_nodes(val)
        if (switch_node.nodes_number() > 0):
            exact_node.set_next(switch_node)

        self._chain = exact_node.find_first_node()

        for i in origin_data:
            if(i in self._unqualify_list_datas):
                pass
            else:
                self._qualify_list_datas.append(i)
        #self._qualify_list_datas = origin_data
        self._temp_chain = None
        self._unhandle_nodes = []
        self._chain_pool = []
        #exact_node.print_chain()

    def _get_normal_nodes(self):
        source = self._temp_chain.find_first_node()
        arr = []
        while (source != None):
            while (source != None and source.get_type() != "normal"):
                source = source.next()
            if (source == None):
                break
            arr.append(source)
            source = source.next()
        return arr

    def _is_origin_data_fit_chain(self,list):
        if(self._temp_chain==None):
            return False
        source = self._temp_chain.find_first_node()
        last_index = 0
        while (source != None):
            while (source != None and source.get_type() != "normal"):
                source = source.next()
            if(source==None):
                break
            marks,unmarks = utils.get_marks(list,source.get_value())
            if(len(marks))==0:
                return False
            else:
                flag = False
                for key2 in range(len(marks)):
                    key1 = marks[key2]
                    if key1[0]<last_index:
                        pass
                    else:
                        last_index = key1[0] + key1[1]
                        flag = True
                        break
                if(flag==False):
                    return False

                source = source.next()
        return True

    def _fit_chain(self,node):
        #check normal ones
        if(self._temp_chain==None):
            return False

        if(node == None):
            raise Exception("sldkjfalskfdj")

        if(self._fit_chain_normal(node)==False):
            return False
        return True

    def _fit_chain_normal(self,node):
        source = self._temp_chain.find_first_node()
        while(source!=None):
            while (source != None and source.get_type() != "normal"):
                source = source.next()
            equal1 = False
            while(node!=None):
                if(node.get_type() != "normal"):
                    node = node.next()
                if(node==None):
                    break
                if(node.equal(source)==False):
                    node = node.next()
                else:
                    equal1 = True
                    node = node.next()
                    break
            if(equal1==False):
                return False
            else:
                source = source.next()
        return True

    def _merge_2_chain(self,chain_node1,chain_node2):
        if(chain_node1==None or chain_node2==None):
            raise Exception("lkjlkjlkjljk")
        #chain_node1.print_chain()
        #chain_node2.print_chain()
        new_chain_node = None
        i = 0
        j = 0
        while(chain_node1!=None):
            while(chain_node2!=None):
                if(chain_node1.equal(chain_node2)):
                    if(i==0 and j==0):
                        if (new_chain_node == None):
                            new_chain_node = chain_node1.clone()
                            pass
                        else:
                            raise Exception("sldkfjlsdkfjs")
                        chain_node1 = chain_node1.next()
                        chain_node2 = chain_node2.next()
                        break
                    else:
                        switch_node = FirstAlgorithmChainNode("switch")

                        #nodes1 = chain_node1.find_all_pre_nodes(i)
                        #nodes2 = chain_node2.find_all_pre_nodes(j)
                        #switch_node.add_nodes(nodes1)
                        #.add_nodes(nodes2)
                        if (new_chain_node == None):
                            pass
                        else:
                            new_chain_node.set_next(switch_node)
                        cn1c = chain_node1

                        switch_node.set_next(chain_node1)

                        new_chain_node = chain_node1

                        break
                else:
                    j+=1
                    chain_node2 = chain_node2.next()
            i+=1
            j=0
            chain_node1=chain_node1.next()
        #new_chain_node.print_chain()

        self._add_chain(new_chain_node)
        #print("123")


    def _add_chain(self,node):
        self._temp_chain = node