public class GA {

        private static final int ChrNum = 4;	//染色体数量
        public static final int GENE = 5; 		//基因
        private static int[] chromosome = {13,24,8,19};//初始化种群


        /*染色体编码，转二进制*/
        private static String chromoCode(int a){
                 String x;
                 int yushu=0;
                 String y="";
                 boolean flag = true;
                 while (flag){
                     yushu=a % 2;
                     a = a / 2;
                     y=yushu+y;
                     if(a<2){
                         y = a+y;
                         if(y.length()<5){
                             for(int n = 0;n<(5-y.length());n++){
                                 y=0+y;
                             }
                         }
                         flag =false;
                     }
                 }
                 x = y;
            return x;
        }

        /*染色体解码，转十进制*/
        public static int bin2(String a) {
            int x;
            int decX = 0; //位数
            for (int j = 0; j < a.length(); j++) {
                int exp = a.charAt(a.length()-j-1) - '0';
                if (exp != 0) {
                    decX += Math.pow(2, j);
                }
            }
            x = decX;
            return x;
        }
        /*求适应度 */
        private int calculatefitnessvalue(String a) {
            int returns;
            returns = bin2(a);
            int y = returns * returns;
            returns = y;

            return returns;
        }

        /*按适应度决定进入下一代的个体*/
        private void select() {
            int evals[] = new int[ChrNum]; // 所有染色体适应值
            double p[] = new double[ChrNum]; // 各染色体选择概率
            double q[] = new double[ChrNum]; // 累计概率
            double F = 0; // 累计适应值总和
            for(int i = 0;i<ChrNum;i++){
                evals[i] = calculatefitnessvalue(chromoCode(chromosome[i]));
            }
            for (int i = 0; i < ChrNum; i++) {
                F = F + evals[i]; // 所有染色体适应值总和
            }
            //求选择概率
            for (int i = 0; i < ChrNum; i++) {
                p[i] = evals[i] / F;
                if (i == 0)
                    q[i] = p[i];
                else {
                    q[i] = q[i - 1] + p[i];
                }
            }
            //和随机数比较
            int[] b = new int[4];
            for (int i = 0; i < ChrNum; i++) {
                double r = Math.random();
                if (r <= q[0]) {
                    b[0]++;
                } else {
                    ok:for (int j = 1; j < ChrNum; j++) {
                        if (r < q[j]) {
                            b[j]++;
                            break ok;
                        }
                    }
                }

            }
            //克隆
            int max = 0,n = 0;
            for(int i = 0;i<ChrNum;i++){
                if(b[i]>max){
                    n = i;
                    max=b[i];
                }
            }
            for(int i = 0;i<ChrNum;i++){
                if(b[i]==0){
                   chromosome[i] = chromosome[n];
                }
            }

        }

        /*交叉操作 交叉率为100%*/
        private void cross() {
            String temp1, temp2;
            int i = 0;
            int m =(int)( Math.random()*5);//随机交叉的位数
            while (i<(ChrNum-1)){
                    temp1 = chromoCode(chromosome[i]).substring(0, m) + chromoCode(chromosome[i+1]).substring(m, 5);
                    temp2 = chromoCode(chromosome[i+1]).substring(0, m) + chromoCode(chromosome[i]).substring(m, 5);
                    chromosome[i]= bin2(temp1);
                    chromosome[i+1] = bin2(temp2);
                    i+=2;

            }
        }

        /*基因突变操作 1%基因变异*/
        private static void mutation() {
            double p = 0.01;
            double mutationNum = GENE*4*p;
            if(mutationNum < 0.1){
               return;
            }
            else {
                int m = (int)(Math.random()*ChrNum);
                StringBuilder sb = new StringBuilder(chromoCode(chromosome[m]));
                sb.replace(m,m+1,"1");
                chromosome[m] = bin2(sb.toString());

            }

        }


        public static void main(String args[]) {
            GA ga = new GA();
            //迭代100次
            ok:for (int i = 0;i<100;i++) {
                ga.select();
                for (int j = 0; j < ChrNum; j++) {
                    if (chromoCode(chromosome[j]).equals("11111")) {
                        System.out.println("迭代次数：" + i + "染色体：" + chromosome[j] + "基因：" + chromoCode(chromosome[j]));
                        break ok;
                    }
                }
                ga.cross();
                for (int j = 0; j < ChrNum; j++) {
                    if (chromoCode(chromosome[j]).equals("11111")) {
                        System.out.println("迭代次数：" + i + "染色体：" + chromosome[j] + "基因：" + chromoCode(chromosome[j]));
                        break ok;
                    }
                }

                ga.mutation();
                for (int j = 0; j < ChrNum; j++) {
                    if (chromoCode(chromosome[j]).equals("11111")) {
                        System.out.println("迭代次数：" + i + "染色体：" + chromosome[j] + "基因：" + chromoCode(chromosome[j]));
                        break ok;
                    }
                }
            }
        }


}
