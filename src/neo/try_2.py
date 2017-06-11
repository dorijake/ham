from neo4j.v1 import GraphDatabase
import json

driver = GraphDatabase.driver("bolt://203.246.82.121:7687", auth=("neo4j", "900416"))

def startSession():
  
  session = driver.session()
  
  return session

# 추후에 createNode로 확장
def createNode_person(session, name, age, sex, belongto, located_in, net_netser_click_num, p_key):
  personDic = {}

  personDic["name"] = str(name)
  personDic["age"] = str(age)
  personDic["sex"] = str(sex)
  personDic["belongto"] = str(belongto)
  personDic["located_in"] = str(located_in)
  personDic["net_netser_click_num"] = str(net_netser_click_num)
  personDic["p_key"] = str(p_key)

  create_person_query = "CREATE (a:Person {name: {name}, age: {age}, sex: {sex}, belongto: {belongto}, located_in:{located_in}, net_netser_click_num:{net_netser_click_num}, p_key:{p_key}})"
  session.run(create_person_query, personDic)

  get_create_result_query = "MATCH (a:Person) WHERE a.p_key = {p_key} RETURN a.name AS name, a.belongto AS belongto"
  result = session.run(get_create_result_query, {"p_key":str(p_key)})

  for record in result:
      print("%s %s" % (record["name"], record["belongto"])) 

def createNode_store(session, name, service_num, service_no, loc_dong_no, loc_gu_no, loc_si_no, p_key):
  storeDic = {}

  storeDic["name"] = str(name)
  storeDic["service_num"] = str(service_num)
  storeDic["service_no"] = str(service_no)
  storeDic["loc_dong_no"] = str(loc_dong_no)
  storeDic["loc_gu_no"] = str(loc_gu_no)
  storeDic["loc_si_no"] = str(loc_si_no)
  storeDic["p_key"] = str(p_key)

  create_store_query = "CREATE (a:Store {name: {name}, service_num: {service_num}, service_no: {service_no}, loc_dong_no:{loc_dong_no}, loc_gu_no:{loc_gu_no}, loc_si_no:{loc_si_no}, p_key:{p_key}})"
  session.run(create_store_query, storeDic)

  get_create_result_query = "MATCH (a:Store) WHERE a.p_key = {p_key} RETURN a.name AS name, a.loc_dong_no AS loc_dong_no"
  result = session.run(get_create_result_query, {"p_key":str(p_key)})

  for record in result:
      print("%s %s" % (record["name"], record["loc_dong_no"])) 

def createNode_group(session, name, group_type_no, p_key):
  groupDic = {}

  groupDic["name"] = str(name)
  groupDic["group_type_no"] = str(group_type_no)
  groupDic["p_key"] = str(p_key)

  create_group_query = "CREATE (a:Group {name: {name}, group_type_no: {group_type_no}, p_key:{p_key}})"
  session.run(create_group_query, groupDic)

  get_create_result_query = "MATCH (a:Group) WHERE a.p_key = {p_key} RETURN a.name AS name, a.group_type_no AS group_type_no"
  result = session.run(get_create_result_query, {"p_key":str(p_key)})

  for record in result:
      print("%s %s" % (record["name"], record["group_type_no"])) 

def createNode_item(session, name, price, incentiveStrg_no, spicy_level, well_level, p_key):
  itemDic = {}

  itemDic["name"] = str(name)
  itemDic["price"] = str(price)
  itemDic["incentiveStrg_no"] = str(incentiveStrg_no)
  itemDic["spicy_level"] = str(spicy_level)
  itemDic["well_level"] = str(well_level)
  itemDic["p_key"] = str(p_key)

  create_store_query = "CREATE (a:Item {name: {name}, price: {price}, incentiveStrg_no:{incentiveStrg_no}, spicy_level:{spicy_level}, well_level:{well_level}, p_key:{p_key}})"
  session.run(create_store_query, itemDic)

  get_create_result_query = "MATCH (a:Item) WHERE a.p_key = {p_key} RETURN a.name AS name, a.incentiveStrg_no AS incentiveStrg_no"
  result = session.run(get_create_result_query, {"p_key":str(p_key)})

  for record in result:
      print("%s %s" % (record["name"], record["incentiveStrg_no"])) 


def deleteNode(session, pgsi, p_key):
  delete_query = "MATCH (a:"+pgsi+") WHERE a.p_key = {p_key} DELETE a"
  result = session.run(delete_query, {"pgsi":str(pgsi), "p_key":str(p_key)})

  print(result) 


# p-key로 할 수 있는 게 아니다
# 
# def deleteRlt(session, rlt):
#   delete_query = "MATCH ()-[r:"+rlt+"]->() WHERE r.p_key = {p_key} DELETE r"
#   result = session.run(delete_query, {"rlt":str(rlt), "p_key":str(p_key)})

#   print(result) 



def createRlt_p2p(session, p1_p_key, p2_p_key, with_num):
  create_query = "MATCH (n:Person) WHERE n.p_key = {p1_p_key} MATCH (m:Person) WHERE m.p_key = {p2_p_key} CREATE (n)-[r:On_rlt_p2p{with_num:{with_num}, last_modified:timestamp()}]->(m)"
  result = session.run(create_query, {"p1_p_key":str(p1_p_key), "p2_p_key":str(p2_p_key), "with_num":str(with_num)})
  create_query = "MATCH (n:Person) WHERE n.p_key = {p2_p_key} MATCH (m:Person) WHERE m.p_key = {p1_p_key} CREATE (n)-[r:On_rlt_p2p{with_num:{with_num}, last_modified:timestamp()}]->(m)"
  result = session.run(create_query, {"p1_p_key":str(p1_p_key), "p2_p_key":str(p2_p_key), "with_num":str(with_num)})
  print(result)
  return

def createRlt_p2g(session, p_p_key, g_p_key, click_num):
  create_query = "MATCH (n:Person) WHERE n.p_key = {p_p_key} MATCH (m:Group) WHERE m.p_key = {g_p_key} CREATE (n)-[r:On_rlt_p2g{click_num:{click_num}, last_modified:timestamp()}]->(m)"
  result = session.run(create_query, {"p_p_key":str(p_p_key), "g_p_key":str(g_p_key), "click_num":str(click_num)})
  print(result)
  return 

def createRlt_p2s(session, p_p_key, s_p_key, wish_on, got_in_num ):
  create_query = "MATCH (n:Person) WHERE n.p_key = {p_p_key} MATCH (m:Store) WHERE m.p_key = {s_p_key} CREATE (n)-[r:On_rlt_p2s{wish_on:{wish_on}, got_in_num:{got_in_num}, last_modified:timestamp()}]->(m)"
  result = session.run(create_query, {"p_p_key":str(p_p_key), "s_p_key":str(s_p_key), "wish_on":str(wish_on), "got_in_num":str(got_in_num)})
  print(result)
  return   

def createRlt_p2i(session, p_p_key, i_p_key, get_num):
  create_query = "MATCH (n:Person) WHERE n.p_key = {p_p_key} MATCH (m:Item) WHERE m.p_key = {i_p_key} CREATE (n)-[r:On_rlt_p2i{get_num:{get_num}, last_modified:timestamp()}]->(m)"
  result = session.run(create_query, {"p_p_key":str(p_p_key), "i_p_key":str(i_p_key), "get_num":str(get_num)})
  print(result)
  return 

# def createRlt_g2p(session, g_p_key, p_p_key):

#   return 0

# def createRlt_g2g(session, g_p_key, g_p_key):
  
#   return 0

# def createRlt_g2s(session, g_p_key, s_p_key):
  
#   return 0 

# def createRlt_g2i(session, g_p_key, i_p_key):
  
#   return 0

# def createRlt_s2p(session, s_p_key, p_p_key):

#   return 

# def createRlt_s2g(session, s_p_key, g_p_key):
  
#   return 

# def createRlt_s2s(session, s_p_key, s_p_key):
  
#   return   

# def createRlt_s2i(session, s_p_key, i_p_key):
  
#   return 

# def createRlt_i2p(session, i_p_key, p_p_key):

#   return 

# def createRlt_i2g(session, i_p_key, g_p_key):
  
#   return 

# def createRlt_i2s(session, i_p_key, s_p_key):
  
#   return   

# def createRlt_i2i(session, i_p_key, i_p_key):
  
#   return 


def select_node_p2p(session, p_key):
  # MATCH (n:Person)-[:On_rlt_p2p]->(m) WHERE n.p_key = "1" RETURN n, m
  create_query = "MATCH (n:Person)-[r:On_rlt_p2p]->(m) WHERE n.p_key = {p_key} RETURN m, r.with_num"
  result = session.run(create_query, {"p_key":str(p_key)})
  got_list = []

  for record in result:
    # m temp_dic
    temp_dic = dict(zip(record.values()[0].keys(), record.values()[0].values()))
    # r.got_in_num : str
    temp_dic["r.with_num"] = int(record.values()[1])
    got_list.append(temp_dic)

   # list sorting by value at dicionaries in list
  sorted_list = sorted(got_list, key = lambda k:k["r.with_num"], reverse = True)

  return sorted_list

def select_node_p2s_got(session, p_key):
  
  create_query = "MATCH (n:Person)-[r:On_rlt_p2s]->(m) WHERE n.p_key = {p_key} RETURN m, r.got_in_num" 
  result = session.run(create_query, {"p_key":str(p_key)})
  got_list = []
  
  for record in result:
    # m temp_dic
    temp_dic = dict(zip(record.values()[0].keys(), record.values()[0].values()))
    # r.got_in_num : str
    temp_dic["r.got_in_num"] = int(record.values()[1])
    got_list.append(temp_dic)

  # list sorting by value at dicionaries in list
  sorted_list = sorted(got_list, key = lambda k:k["r.got_in_num"], reverse = True)

  return sorted_list

def select_node_psp_1(session, p_p_key):
  got_list = []

  for store in select_node_p2s_got(session, p_p_key):
    temp = {}
    temp["people"] = select_node_s2p_net(session, store["p_key"], p_p_key)
    temp["storename"] = store["name"]
    
    got_list.append(temp)
    
  # [ [ storename dic (가게 이름) + people dic (간 친구들 목록) ] , [  다른 가게에 대해 ]]
  return got_list


#p_p_key 의 친구들이 자주 가는 가게들
#그리고 가게별 이용하는 친구들
def select_node_f2p(session, p_p_key):
  storedic = {}

  for friend in select_node_p2p(session, p_p_key):

    for store in select_node_p2s_got(session, friend["p_key"]):
      friends_by_store = {"name" : friend["name"], "p_key" : friend["p_key"], "r.got_in_num" : store["r.got_in_num"]}

      if store["name"] in storedic :
        storedic[store["name"]].append(friends_by_store)
      if store["name"] not in storedic : 
        storedic[store["name"]] = []
        storedic[store["name"]].append(friends_by_store)
        
  for storename in storedic.keys():
    storedic[storename] = sorted(storedic[storename], key = lambda k:k["r.got_in_num"], reverse = True)  
  
  storescore = {}
  storescorelist = []
  
  for store in storedic.keys():
    score = 0
    for storedata in storedic[store] :
      score += int(storedata["r.got_in_num"])
    storescore[store] = score

    storescorerank = sorted(storescore, key=storescore.__getitem__, reverse = True)

  got_list = [storescorerank, storedic]
  
  #got_list[0] : 인기 많은 store sorted list
  #got_list[1] : 딕셔너리. keys = 가게이름, values = 가게 이용한 친구들에 대한 딕셔너리 (p_key, name, r.got_in_num 3가지. sorted by got_in_num)
  
  return got_list

# 현재 s2p 관계를 정의하지 않았기 때문에 p2s 에 대한 관계를 이용해서 꾸림
def select_node_s2p(session, p_key, p_p_key):

  create_query = "MATCH (n:Store)-[r:On_rlt_p2s]-(m:Person) WHERE n.p_key = {p_key} RETURN m, r.got_in_num" 
  result = session.run(create_query, {"p_key":str(p_key)})
  got_list = []

  for record in result:

    # 본인을 제외함 p_p_key 걸러내기
    if record.values()[0].get("p_key") == p_p_key : continue
    temp_dic = dict(zip(record.values()[0].keys(), record.values()[0].values()))
    # r.got_in_num : str
    temp_dic["r.got_in_num"] = int(record.values()[1])
    got_list.append(temp_dic) 

  # [한 사람의 정보 + 가게 간 횟수 (got_in_num), ]
  return got_list

# 본인를 제외하고, 자신과 관계 있는 사람들만 가져옴
def select_node_s2p_net(session, p_key, p_p_key):

  create_query = "MATCH (n:Store)-[r:On_rlt_p2s]-(m:Person) WHERE n.p_key = {p_key} RETURN m, r.got_in_num" 
  result = session.run(create_query, {"p_key":str(p_key)})
  got_list = []

  for record in result:
    # 본인을 제외함 p_p_key 걸러내기
    if record.values()[0].get("p_key") == p_p_key : continue
    # 친구만 남기기
    for person in select_node_p2p(session, p_p_key):
      if record.values()[0].get("p_key") == person["p_key"]:
        temp_dic = dict(zip(record.values()[0].keys(), record.values()[0].values()))
        temp_dic["r.got_in_num"] = int(record.values()[1])
        # r.got_in_num : str
        got_list.append(temp_dic)
    
  # [한 사람의 정보 + 가게 간 횟수 (got_in_num), ]
  return got_list

def encode2json_d3_first(sorted_list):
  name_list_sorted_gotInNum = []

  for store in sorted_list:
    name_list_sorted_gotInNum.append(store["name"])
  
  temp_dic = {}
  temp_dic["nodes"] = name_list_sorted_gotInNum
  print(json.dumps(temp_dic,ensure_ascii=False))



def select_node_p2s_wish(session, p_key):
  create_query = "MATCH (n:Person)-[r:On_rlt_p2s]->(m) WHERE n.p_key = {p_key}, r.wish_on = \"1\" ORDER BY = r.got_in_num DESC RETURN m"
  result = session.run(create_query, {"p_key":str(p_key)})
  r_dic = []
  p_dic = {}
  v_dic = {}
  for record in result:
    print(result)

def service_00_p2s():
  print("a")



session = startSession()

#createNode_person(session, name, age, sex, belongto, located_in, net_netser_click_num, p_key):
# createNode_person(session, "김민석", "28", "1", "서울과학기술대학교", "1", "10", "1")
# createNode_person(session, "박종균", "27", "1", "서울과학기술대학교", "0", "10", "2")
# createNode_person(session, "민연홍", "25", "1", "서울과학기술대학교", "1", "10", "3")
# createNode_person(session, "조우영", "21", "1", "서울과학기술대학교", "1", "10", "4")
# createNode_person(session, "한동기", "24", "1", "서울과학기술대학교", "0", "10", "5")
# createNode_person(session, "박제익", "22", "1", "서울과학기술대학교", "0", "10", "6")
# createNode_person(session, "박준형", "22", "1", "서울과학기술대학교", "0", "10", "7")
# createNode_person(session, "문재인", "65", "1", "청와대", "0", "10", "8")

# createNode_item(session, "부대찌개", "6000", "001", "3", "2", "00000010")
# 
# def createNode_store(session, name, service_num, service_no, loc_dong_no, loc_gu_no, loc_si_no, p_key):
# createNode_store(session, "밥은", "0001", "0001", "공릉동", "노원구", "서울시", "00000007")
# createNode_store(session, "소문날라", "0001", "0001", "공릉동", "노원구", "서울시", "00000008")
# createNode_store(session, "호야네", "0002", "0001", "공릉동", "노원구", "서울시", "00000009")
# createNode_store(session, "호치킨", "0000", "0001", "공릉동", "노원구", "서울시", "00000010")
# createNode_store(session, "맥도날드", "0003", "0001", "공릉동", "노원구", "서울시", "00000011")
# createNode_store(session, "신서방 족발", "0000", "0001", "공릉동", "노원구", "서울시", "00000012")
# createNode_store(session, "Hippo Coffe", "0001", "0001", "공릉동", "노원구", "서울시", "00000013")

# #createNode_group(session, name, group_type_no, p_key):
# createNode_group(session, "캡사이숑", "8", "11111111" )
# createNode_group(session, "직공팀", "8", "22222222" )

# # deleteNode(session, "Person", "8")
# deleteRlt(session, rlt, p_key):


# createRlt_p2p(session, "1", "2", "3")
# createRlt_p2p(session, "1", "8", "3")
# createRlt_p2p(session, "1", "3", "3")
# createRlt_p2p(session, "2", "3", "3")
# createRlt_p2g(session, "5", "11111111", "3")
# createRlt_p2s(session, "5", "00000007", "1", "0")
# createRlt_p2s(session, "5", "00000008", "0", "5")
# createRlt_p2s(session, "5", "00000009", "0", "6")
# createRlt_p2s(session, "5", "00000010", "1", "0")
# createRlt_p2s(session, "5", "00000011", "0", "11")
# createRlt_p2s(session, "5", "00000012", "1", "0")
# createRlt_p2s(session, "5", "00000013", "0", "10")
# createRlt_p2i(session, "5", "00000010", "3")
# createRlt_p2i(session, "6", "00000010", "3")

# print(select_node_f2p(session,"1")[0])
print(encode2json_d3_first(select_node_f2p(session,"1")[1]))
# print(select_node_s2p_net(session, "00000007", "1"))
# print(select_node_psp_1(session, "1"))
# print(select_node_s2p(session, "00000009", "4"))
# print(select_node_p2p(session, "1"))
# encode2json_d3_first(select_node_p2s_got(session, "5"))
# print_friends_of(session, "2")

session.close()