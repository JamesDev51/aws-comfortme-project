import pymysql
DB_HOST="db-team8-consolation.c8fut6pj2ay8.ap-northeast-2.rds.amazonaws.com"
DB_USER="root"
DB_PASSWORD="1tkddydwkdql"
DB_NAME="comfortmeDB"

def getMysqlConn():
    return pymysql.connect(
            host=DB_HOST, 
            user=DB_USER, 
            password=DB_PASSWORD, 
            db=DB_NAME)

def  conductSqlQuery(sql, sqlData):
    print("--------------------------------")
    print("conductSqlQuery function init")
    conn=getMysqlConn()
    curs = conn.cursor()
    curs.executemany(sql, sqlData)
    conn.commit()
    print("conductSqlQuery function done")
    print("--------------------------------")
    
sql = "INSERT INTO ConsolePost(title,contents,email,anonymous,mainCategory,subCategory,positive,negative) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"




sqlData=[('제목입니다','제 감정이 이상해진 것 같아요. 남편만 보면 화가 치밀어 오르고 감정 조절이 안되요.            ','daehwa001210@gmail.com','1','감정','감정조절이상','0.1234','0.907'),
('제목입니다','더 이상 내 감정을 내가 컨트롤 못 하겠어.                                       ','daehwa001210@gmail.com','1','감정','감정조절이상','0.1234','0.907'),
('제목입니다','하루종일 오르락내리락 롤러코스터 타는 기분이에요.                                   ','daehwa001210@gmail.com','1','감정','감정조절이상','0.1234','0.907'),
('제목입니다','꼭 롤러코스터 타는 것 같아요.                                               ','daehwa001210@gmail.com','1','감정','감정조절이상','0.1234','0.907'),
('제목입니다','롤러코스터 타는 것처럼 기분이 왔다 갔다 해요.                                     ','daehwa001210@gmail.com','1','감정','감정조절이상','0.1234','0.907'),
('제목입니다','작년 가을부터 감정조절이 잘 안 되는 거 같아.                                     ','daehwa001210@gmail.com','1','감정','감정조절이상','0.1234','0.907'),
('제목입니다','예전에 비해서 인내심이 너무 짧아진 거 같아.                                      ','daehwa001210@gmail.com','1','감정','감정조절이상','0.1234','0.907'),
('제목입니다','더 이상 혼자서는 감정조절을 못하겠어.                                          ','daehwa001210@gmail.com','1','감정','감정조절이상','0.1234','0.907'),
('제목입니다','점점 나 자신을 컨트롤하지 못하는 기분이야.                                       ','daehwa001210@gmail.com','1','감정','감정조절이상','0.1234','0.907'),
('제목입니다','나도 이러기 싫은데 내 마음대로 안돼.                                           ','daehwa001210@gmail.com','1','감정','감정조절이상','0.1234','0.907'),
('제목입니다','맨정신일 때는 저를 주체할 수 가 없었거든요.                                      ','daehwa001210@gmail.com','1','감정','감정조절이상','0.1234','0.907'),
('제목입니다','주체가 안 돼.                                                          ','daehwa001210@gmail.com','1','감정','감정조절이상','0.1234','0.907'),
('제목입니다','이렇게 쌓이고 쌓이다 나중에 확 터지거든요. 진짜 걷잡을 수 없이요.                       ','daehwa001210@gmail.com','1','감정','감정조절이상','0.1234','0.907'),
('제목입니다','근데 감정을 다스리지 못해 욱하기도하고.                                         ','daehwa001210@gmail.com','1','감정','감정조절이상','0.1234','0.907'),
('제목입니다','순간순간 감정조절을 못해요.                                                 ','daehwa001210@gmail.com','1','감정','감정조절이상','0.1234','0.907'),
('제목입니다','평소 다른 일을 할 때도 비슷해요. 생각한대로 안되면 화가 나고…그런 상황이 지속되면 폭발해버려요.  ','daehwa001210@gmail.com','1','감정','감정조절이상/화   ','0.1234','0.907'),
('제목입니다','예전보다 화내는 게 과격해진 거 같아.                                           ','daehwa001210@gmail.com','1','감정','감정조절이상/화   ','0.1234','0.907'),
('제목입니다','화가 안 참아져.                                                         ','daehwa001210@gmail.com','1','감정','감정조절이상/화   ','0.1234','0.907'),
('제목입니다','근데 다음에 또 그러면 또 화가 나고… 모르겠어요. 제 감정이 통제가 안 돼요.                ','daehwa001210@gmail.com','1','감정','감정조절이상/화   ','0.1234','0.907'),
('제목입니다','마음은 안 그런데 화를 낼 때 더 불같이 내게 되기도 하고..                            ','daehwa001210@gmail.com','1','감정','감정조절이상/화   ','0.1234','0.907'),
('제목입니다','막 내 감정을 내가 주체 못 한다나? 화 내는 게 뭔가 평소랑 다르대.                      ','daehwa001210@gmail.com','1','감정','감정조절이상/화   ','0.1234','0.907')]

conductSqlQuery(sql,sqlData)