USE air
GO
INSERT INTO ����(��������,������,���ڳ���)
VALUES
('01','�׶�����','����'),
('02','˫������','�ɶ�'),
('03','�������','���'),
('04','�׶�����','����'),
('05','̫ƽ����','������'),
('06','��������','����'),
('07','�׶�����','����'),
('08','���Ż���','�Ϻ�'),
('09','���λ���','����'),
('10','�д�����','����'),
('11','���ƻ���','����'),
('12','��ɳ����','��ɳ'),
('13','��������','�ϲ�'),
('14','��Է����','����'),

INSERT INTO �û���(�û���
      ,�û�����
      ,�û�Ȩ��
      ,�û���ϵ��ʽ)
VALUES
('������ѧ','310226199',0,'1321231278'),
('�Ϻ����Ļ���','31022612873',0,'18888888888'),
('֣���̲�԰','zzlby2010',0,'13543276895'),
('����','1274111',0,'18917260800'),
('��ƽ��~','dpx123321',0,'1891739856'),
('����','1274111',0,'18917260800'), 
('���а�','seiclhiqcaa',0,'13876392037'),
('aa','asdfghjkl',0,'18217461800'),
('��������Աa','kseh23Gke9',1,'13972654267'),
('��������Աb','AShs195ose',1,'13232604267'),
('����Աa','123456',2,'13972397267')	        

INSERT INTO ����(������,������������,��ͣ��������,�����������)
VALUES
('0001','01',null,'02'),
('0002','01',null,'03'),
('0003','05','12','06'),     
('0004','08',null,'09'),
('0005','08','12','10'),
('0006','14',null,'11'),
('0007','01',null,'02'),
('0008','01',null,'12'),
('0009','01',null,'13')
/*���зɻ��������԰ٶȰٿƣ���������λΪ�֣������̵�λΪǧ��*/
INSERT INTO �ɻ���
VALUES
('�տ�319',0,8,120,68,7200),
('�տ�321',12,0,173,83,5600),
('�տ�330',20,16,255,230,7400),
('����747',42,8,261,148,13890),
('����777',54,15,299,178,12400)

INSERT INTO �ɻ��Ǽ�
VALUES
('001','�տ�319',2015-08-01,5,null),
('002','�տ�319',2015-08-01,5,null),
('003','�տ�319',2015-08-01,5,null),
('004','�տ�321',2016-09-01,4,null),
('005','�տ�321',2016-09-01,4,null),
('006','�տ�321',2016-09-01,4,null),
('007','�տ�330',2017-10-22,3,null),
('008','�տ�330',2017-10-22,3,null),
('009','�տ�330',2017-10-22,3,null),
('010','����777',2014-01-01,6,null),
('011','����777',2014-01-01,6,null),
('012','����777',2014-01-01,6,null),
('013','����747',2018-01-01,2,null),
('014','����747' ,2018-01-01,2,null),
('015','����747',2018-01-01,2,null)

INSERT INTO �ɻ�����
VALUES
('0001','001'),
('0001','002'),
('0002','003'),
('0003','004'),
('0003','005'),
('0003','006'),
('0004','007'),
('0006','008'),
('0006','009'),
('0005','010'),
('0005','011'),
('0005','012'),
('0007','013'),
('0008','014'),
('0009','015')

INSERT INTO ��Ʊ
VALUES
(1,'�׶�����','˫������','001','���ò�','����','������','��','����','411002196402122371','13837439823'),
(1,'�׶�����','˫������','002','���ò�','��ƽ��~','����','��','�м�','411001199902122391','13837434523'),
(4,'�׶�����','�������','001','���ò�','����','��ɿ�','Ů','С��','311002201402122381','13823879823'),
(4,'�׶�����','�������','002','���ò�','����','���','��','����','311002197302122311','13823879823'),
(5,'�׶�����','�������','001','�����','����','����','Ů','����','311002197603132481','13928376273'),
(6,'̫ƽ����','��������','001','���ò�','����','����','��','С��','411001201702122371','13829386483'),
(6,'̫ƽ����','��ɳ����','002','���ò�','����','�Źⱱ','��','����','321001198603022371','13922946483'),
(10,'���Ż���','��������','001','���ò�','������ѧ','����','��','����','411001198412212371','15723126483'),
(10,'��������','�д�����','002','�����','������ѧ','����','��','����','411001198809212331','15629386483'),
(16,'�׶�����','��ɳ����','001','ͷ�Ȳ�','aa','�µ�','Ů','����','312001199302122362','15702986483'),
(17,'�׶�����','��������','001','���ò�','֣���̲�԰','����ٻ','Ů','����','411001196802222381','17827362817'),
(17,'�׶�����','��������','002','���ò�','�Ϻ����Ļ���','�����','��','����','332001199409122372','13892836483')
GO

/*�������2019��1��1��Ϊ�����գ�������2019���һ���ڵķ��мƻ����ţ����ɴ�����ȫ�ꣻ����Ϊ����϶�Ʊ�����Ѿ���ʣ��Ʊ�����˴���*/
INSERT INTO ���мƻ�����(������,�ƻ�����ʱ��,�ƻ����ﾭͣ����ʱ��,�ƻ��Ӿ�ͣ��������ʱ��,�ƻ�����ʱ��,"���òգ���ʼ-���ʣ����λ","����գ���ʼ-���ʣ����λ","ͷ�Ȳգ���ʼ-���ʣ����λ","���òգ���ͣ-���ʣ����λ","����գ���ͣ-���ʣ����λ","ͷ�Ȳգ���ͣ-���ʣ����λ","���òգ���ʼ-��ͣ��ʣ����λ","����գ���ʼ-��ͣ��ʣ����λ","ͷ�Ȳգ���ʼ-��ͣ��ʣ����λ","Ʊ�ۣ���ʼ-������òգ�","Ʊ�ۣ���ʼ-��ͣ�����òգ�","Ʊ�ۣ���ͣ-������òգ�","Ʊ�ۣ���ʼ-�������գ�","Ʊ�ۣ���ʼ-��ͣ������գ�","Ʊ�ۣ���ͣ-�������գ�","Ʊ�ۣ���ʼ-���ͷ�Ȳգ�","Ʊ�ۣ���ʼ-��ͣ��ͷ�Ȳգ�","Ʊ�ۣ���ͣ-���ͷ�Ȳգ�")
VALUES
('0001','2019-01-01 08:00:00',null,null,'2019-01-01 10:30:00',118,0,8,null,null,null,null,null,null,500,null,null,800,null,null,1100,null,null),
('0001','2019-01-03 08:00:00',null,null,'2019-01-01 10:30:00',120,0,8,null,null,null,null,null,null,500,null,null,800,null,null,1100,null,null),
('0001','2019-01-05 08:00:00',null,null,'2019-01-01 10:30:00',120,0,8,null,null,null,null,null,null,500,null,null,800,null,null,1100,null,null),
('0002','2019-01-02 13:00:00',null,null,'2019-01-02 16:30:00',118,0,8,null,null,null,null,null,null,500,null,null,800,null,null,1100,null,null),
('0002','2019-01-06 13:00:00',null,null,'2019-01-06 16:30:00',120,0,7,null,null,null,null,null,null,500,null,null,800,null,null,1100,null,null),
('0003','2019-01-01 10:00:00','2019-01-01 12:00:00','2019-01-01 13:00:00','2019-01-01 14:30:00',172,12,0,171,12,0,172,12,0,500,300,200,800,600,500,1100,900,800),
('0003','2019-01-04 10:00:00','2019-01-04 12:00:00','2019-01-04 13:00:00','2019-01-04 14:30:00',173,12,0,173,12,0,173,12,0,500,300,200,800,600,500,1100,900,800),
('0003','2019-01-07 10:00:00','2019-01-07 12:00:00','2019-01-07 13:00:00','2019-01-07 14:30:00',173,12,0,173,12,0,173,12,0,500,300,200,800,600,500,1100,900,800),
('0004','2019-01-05 17:00:00',null,null,'2019-01-05 20:30:00',255,20,16,null,null,null,null,null,null,670,null,null,970,null,null,1270,null,null),
('0005','2019-01-01 15:00:00','2019-01-01 17:00:00','2019-01-01 18:00:00','2019-01-01 20:30:00',260,41,8,260,42,8,260,41,8,600,300,300,900,450,450,1200,600,600),
('0005','2019-01-04 15:00:00','2019-01-04 17:00:00','2019-01-04 18:00:00','2019-01-04 20:30:00',261,42,8,261,42,8,261,42,8,600,300,300,900,450,450,1200,600,600),
('0005','2019-01-07 15:00:00','2019-01-07 17:00:00','2019-01-07 18:00:00','2019-01-07 20:30:00',261,42,8,261,42,8,261,42,8,600,300,300,900,450,450,1200,600,600),
('0006','2019-01-02 08:00:00',null,null,'2019-01-02 13:30:00',255,20,16,null,null,null,null,null,null,670,null,null,1100,null,null,1570,null,null),
('0006','2019-01-06 08:00:00',null,null,'2019-01-06 13:30:00',255,20,16,null,null,null,null,null,null,670,null,null,1100,null,null,1570,null,null),
('0007','2019-01-03 09:30:00',null,null,'2019-01-03 13:00:00',299,54,15,null,null,null,null,null,null,670,null,null,970,null,null,1270,null,null),
('0008','2019-01-04 08:30:00',null,null,'2019-01-04 10:30:00',299,54,14,null,null,null,null,null,null,400,null,null,700,null,null,1000,null,null),
('0009','2019-01-06 11:30:00',null,null,'2019-01-03 15:00:00',297,54,15,null,null,null,null,null,null,570,null,null,870,null,null,1170,null,null)
GO