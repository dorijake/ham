from neo4j.v1 import GraphDatabase

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



def createRlt_p2p(session, p1_p_key, p2_p_key, with_num):
  create_query = "MATCH (n:Person) WHERE n.p_key = {p1_p_key} MATCH (m:Person) WHERE m.p_key = {p2_p_key} CREATE (n)-[r:On_rlt_p2p{with_num:{with_num}, last_modified:timestamp()}]->(m)"
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


session = startSession()

#createNode_person(session, name, age, sex, belongto, located_in, net_netser_click_num, p_key):
createNode_person(session, "김민석", "28", "1", "서울과학기술대학교", "1", "10", "1")
createNode_person(session, "박종균", "27", "1", "서울과학기술대학교", "0", "10", "2")
createNode_person(session, "민연홍", "25", "1", "서울과학기술대학교", "1", "10", "3")
createNode_person(session, "조우영", "21", "1", "서울과학기술대학교", "1", "10", "4")
createNode_person(session, "한동기", "24", "1", "서울과학기술대학교", "0", "10", "5")
createNode_person(session, "박제익", "22", "1", "서울과학기술대학교", "0", "10", "6")
createNode_person(session, "박준형", "22", "1", "서울과학기술대학교", "0", "10", "7")

createNode_item(session, "부대찌개", "6000", "001", "3", "2", "00000010")
createNode_store(session, "밥은", "0001", "0001", "공릉동", "노원구", "서울시", "00000007")

#createNode_group(session, name, group_type_no, p_key):
createNode_group(session, "캡사이숑", "8", "11111111" )

# deleteNode(session, "Group", "11111111")

# createRlt_p2p(session, "5", "6", "3")
# createRlt_p2g(session, "5", "11111111", "3")
# createRlt_p2s(session, "5", "00000007", "1", "0")
createRlt_p2i(session, "5", "00000010", "3")
createRlt_p2i(session, "6", "00000010", "3")

session.close()