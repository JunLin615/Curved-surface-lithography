//电机1为旋转电机，电机2为平移电机，
//电机1的旋转、方向、使能定义
#define STEP1 5
#define DIR1 6
#define EN1 7
//电机2的旋转、方向、使能定义
#define STEP2 8
#define DIR2 9
#define EN2 10
//光电开关模拟输入端口定义
//ADpin1对应左1，遮挡触发时视为左侧平移极限
//ADpin2对应左2，遮挡触发时视为右侧平移极限
//ADpin3对应左3，遮挡触发时视为零点
#define ADpin1 A0
#define ADpin2 A1
#define ADpin3 A2
//Lead为丝杆导程，单位10um，即1000个10um=10mm根据使用丝杆导轨型号而定义
#define Lead 1000
//Subdivision1为电机1细分，Subdivision2为电机2细分，可通过驱动器设置调节
#define Subdivision1 1000
#define Subdivision2 1000

void setup() {
  // put your setup code here, to run once:
pinMode(STEP1,OUTPUT);
pinMode(DIR1,OUTPUT);
pinMode(EN1,OUTPUT);
pinMode(STEP2,OUTPUT);
pinMode(DIR2,OUTPUT);
pinMode(EN2,OUTPUT);

Serial.begin(9600);
}
//光电开关模拟输入信号
int ADBuffer1 = 0;
int ADBuffer2 = 0;
int ADBuffer3 = 0;

boolean prohibit_l = false;//左侧平移极限预警
boolean prohibit_r = false;//右侧平移极限预警
boolean prohibit_0 = false;//零点预警
boolean suspend_signal = false;//暂停信号
boolean Mobile_state = false;//true右，false左

boolean rotate_state = false;//电机1是否旋转，true转，false不转


int speed1 = 2;//电机1转速每秒圈数
long displacement = 30000;//平移距离，单位10um,300mm=30000*10um
//int velocity2 = 100;//平移速度，单位10um/s

String comdata = "";//字符串数据
String comdata_l = "";//临时字符串数据
int commaPosition;//存储还没有分离出来的字符串
short Command_type = 0;//存储指令类型1:经典加工，0：复位。2暂停，3重启。
unsigned int delayu;//时间延迟，与速度有关
unsigned int Steps;//步数，与路程有关
unsigned int frequency1;//电机1频率

void loop()
{
  // put your main code here, to run repeatedly:
  Read_command();//通过串口接收指令，无指令则一直循环不进入下一步。
  Understanding();//从指令提取数值并赋值给speed1、displacement、velocity2
  if(Command_type==1)
  {
    Classic_processing();//执行经典加工
  }   
  }
   

void Classic_processing()
{
  frequency1 = speed1*Subdivision1;
  tone(STEP1,  frequency1);//控制电机1转动
  translation(displacement);
  noTone(STEP1);
  Serial.println("end");//完成步骤
}

void OneStep(int em)
{
  //em为要进行单步移动的电机号
  //delayu为单步移动时高低电平持续时间，单位us
  int STEP;
  if(em==1){
    STEP=STEP1;
  }
  if(em==2){
    STEP=STEP2;
  }
  
  if(delayu>1000)
  {
    unsigned int delaym;
    delaym = delayu/1000;
    digitalWrite(STEP,HIGH);
    delay(delaym);
    digitalWrite(STEP,LOW);
    delay(delaym);
    }
    else
    {  
      digitalWrite(STEP,HIGH);
      delayMicroseconds(delayu);
      digitalWrite(STEP,LOW);
      delayMicroseconds(delayu);
    }

}

void translation(long displacement)
{
  //displacement为要平移的距离，单位10um，正右负左
  //delayu为单步移动时高低电平持续时间，单位us，和移动速度有关
  if(displacement>0)
  {
    digitalWrite(DIR2,LOW);//右平移，无电机方向
    Mobile_state=true;//true右
   }
   if(displacement<0)
   {
    digitalWrite(DIR2,HIGH);//左平移，电机方向
    displacement=0-displacement;
    Mobile_state = false;//false左
   }
  
  Steps=displacement;//路程/导程=圈数，圈数*细分=步数
  //Steps=displacement/Lead*Subdivision2;//路程/导程=圈数，圈数*细分=步数
  
  //delayu = 10000/(velocity2/Lead*Subdivision2*2)*100;
  Serial.print("delayu");
  Serial.println(delayu);
  for(int i=1; i <= Steps; i++)
  {
    Limit_detection();
    if(Serial.available()>0)
    {
     suspend();
     Understanding();
     while(suspend_signal)
     {
      Serial.print("2S");
      suspend();
      Understanding();
     }
      }
    if(Mobile_state)
    {
      //右移状态
      if(prohibit_r)
      {
        Serial.print("Rl");//右侧已到极限，无法继续右移
        break;
        }
     }
    else
    {
      //左移状态
      if(prohibit_l)
      {
        //限位预警true则跳出循环，不执行移动。
        Serial.print("Ll");//左侧已达极限，无法继续左移
        break;
        }
     }

     
    OneStep(2);
   }
  
}
void translation_r(long displacement)
{
  //displacement为要平移的距离，单位10um，正右负左
  //delayu为单步移动时高低电平持续时间，单位us，和移动速度有关
  if(displacement>0)
  {
    digitalWrite(DIR2,LOW);//右平移，无电机方向
    Mobile_state=true;//true右
   }
   if(displacement<0)
   {
    digitalWrite(DIR2,HIGH);//左平移，电机方向
    displacement=0-displacement;
    Mobile_state = false;//false左
   }

  Steps=displacement/Lead*Subdivision2;
  //delayu = 1000/(velocity2/Lead*Subdivision2*2)*100;
  for(int i=1; i <= Steps; i++)
  {
    Limit_detection();
    if(Mobile_state)
    {
      //右移状态
      if(prohibit_r)
      {
        Serial.print("Rl");//右侧已到极限，无法继续右移
        break;
        }
     }
    else
    {
      //左移状态
      if(prohibit_0)
      {
        //限位预警true则跳出循环，不执行移动。
        Serial.print("to0end");//已经到达零点
        break;
        }
     }
    Step0();
   }
  
}
void Limit_detection()
{
   ADBuffer1 = analogRead(ADpin1);//读取左1光电开关信号,无遮1023，遮挡0
   ADBuffer2 = analogRead(ADpin2);//读取左3光电开关信号
   ADBuffer3 = analogRead(ADpin3);//读取左2(0点)光电开关信号
   if(ADBuffer1<800)
   {
      prohibit_l = true;//左侧限位判断
    }
    else
    {
      prohibit_l = false;
    }
     
   if(ADBuffer2<800)
   {
      prohibit_r = true;//右侧限位判定
    }
   else
   {
      prohibit_r = false;
    }  
   if(ADBuffer3<800)
   {
      prohibit_0 = true;//右侧限位判定
    }
   else
   {
      prohibit_0 = false;
    }
}
void reset()
{
  //此函数用于复位于零点。
  translation_r(50000);//先右移至右侧限位。
  delay(500);
  translation_r(-50000);//左移至零点限位。
  Serial.print("0");//已经达到零点。
}
void Read_command()
{ 
  //用于读取上位机命令
  while(Serial.available()==0)
  {
  delay(2);
  }
  comdata="";
  //String comdata="";//字符串数据
   while(Serial.available()>0)
  {
      comdata += char(Serial.read());//叠加数据到comdata
      delay(2);//延时等待响应
   }  
}
void suspend()
{
     comdata="";
     while(Serial.available()>0)
    {
        comdata += char(Serial.read());//叠加数据到comdata
        delay(2);//延时等待响应
    }
}
  
void Understanding()
{
  comdata_l = comdata.substring(0,1)[0];
  Command_type=comdata_l.toInt();//[0,9],步长1
  switch (Command_type) 
  { 
    case   0:
                reset();
                break;
    case   1:
                //Serial.println(Command_type);
                comdata_l = comdata.substring(1,2);
                speed1=comdata_l.toInt();//[0,9],步长1
                
                comdata_l=comdata.substring(2,7);
                delayu=comdata_l.toInt();//[0,20000],步长1.即
                //Serial.print("delayu");
                //Serial.println(delayu);
                comdata_l=comdata.substring(7,13);
                displacement=comdata_l.toInt();//
                //当 var 等于 1 时，执行一些语句
                break;
    case   2:
                suspend_signal=true;//暂停
                Serial.print("2");
                //当 var 等于 2 时，执行一些语句
                break;   
    case   3:
                suspend_signal=false;//取消暂停
                Serial.print("3");
                //当 var 等于 3 时，执行一些语句
                break;
    case   4:
                comdata_l = comdata.substring(1,2);
                speed1=comdata_l.toInt();//[0,9],步长1

                frequency1 = speed1*Subdivision1;
                tone(STEP1,  frequency1);

                 break;
    case   5:
                  //5(12)(123)：5(电机号)(左停右)
                  int DIR;
                  int em;
                  
                  comdata_l = comdata.substring(1,2);
                 
                  if(comdata_l.toInt()==1)
                  {
                     DIR = DIR1;
                     em=1;
                     noTone(STEP1);
                     
                   }
                  if(comdata_l.toInt()==2)
                  {
                   DIR = DIR2;
                   em=2;
                   }
                   comdata_l = comdata.substring(2,3);
                  if(comdata_l.toInt()==1)
                  {
                    digitalWrite(DIR,HIGH);//左平移
                    OneStepT(em);
                   }
                  if(comdata_l.toInt()==2)
                  {
                   delayMicroseconds(10);;//不平移
                   }
                   if(comdata_l.toInt()==3)
                  {
                   digitalWrite(DIR,LOW);//右平移
                   OneStepT(em);
                   }
                   break;
  }
}
void Step0()
{

  digitalWrite(STEP2,HIGH);
  delayMicroseconds(5);
  digitalWrite(STEP2,LOW);
  delayMicroseconds(5);
}
void OneStepT(int em)
{
  //em为要进行单步移动的电机号

  int STEP;
  if(em==1){
    STEP=STEP1;
  }
  if(em==2){
    STEP=STEP2;
  }
  digitalWrite(STEP,HIGH);
  delayMicroseconds(5);
  digitalWrite(STEP,LOW);
  delayMicroseconds(5);

}
