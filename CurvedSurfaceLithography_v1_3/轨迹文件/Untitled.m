%% ���������ע�ⵥλ
delayed = 500;%ms,ÿ����ʱ���������20ms��
processing_length = 2;%��λmm���ӹ����ȣ����𳬹�100mm��
pitch = 100;%��λum���ݾ�

%% ������룬�����޸�
t_steps =processing_length*1000/10;%ƽ�Ʋ�����һ��10um

t_steps_i = t_steps*2;
t=1:t_steps_i;%1000��10um,10mm
%r=1:5:5000;
%r = 1:10:10000;
pitch_r = pitch/10 ;%250*10um =250um=0.25mm
c = t_steps_i/pitch_r;%Ȧ��
r_steps = c*1000;%��ת������
intermediary = r_steps/t_steps_i;
r = 1:intermediary:r_steps;


%r1= 1:1:5000;
r1_l=  1:1:r_steps;
t1_l = round(interp1(r,t,r1_l));

r1 = r1_l(1:r_steps/2);
t1 = t1_l(1:r_steps/2);


%plot(r,t,"o")
%hold on
%plot(r1,t1,"*")


td=diff(t1)+2;
rd=diff(r1)+2;

rd_r = rd';
td_r= td';
len_r = length(td_r(:));

delayed_r = ones(len_r,1).*delayed;
%plot(td,"o");
%figure;
%plot(rd,"o")
data_r = [rd_r,td_r,delayed_r];
csvwrite('aaa.csv',data_r)