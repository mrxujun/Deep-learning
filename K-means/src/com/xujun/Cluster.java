package com.xujun;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;

public class Cluster {
    private  Point point;
    //两个簇
    List<Point> cluster1 = new ArrayList<>();
    List<Point> cluster2 = new ArrayList<>();

    public void cluster(List<Point> list,double centerX1,double centerX2,double centerY1,double centerY2){
         //计算每个点到K个中心的距离
        for (Point point : list) {
           if(getEuclideanDis(point,centerX1,centerY1) <= getEuclideanDis(point,centerX2,centerY2)){
             cluster1.add(point);
           }
           else {
             cluster2.add(point);
           }
        }
        //计算每个簇的中心
        double center_x3 = CenterX(cluster1);
        double center_x4 = CenterX(cluster2);
        double center_y3 = CenterY(cluster1);
        double center_y4 = CenterY(cluster2);
        double cen_dis1 =Math.sqrt((centerX1 -center_x3) * (centerX1 -center_x3)+(centerY1 - center_y3)*(centerY1 -center_y3));
        double cen_dis2 =Math.sqrt((centerX2 -center_x4) * (centerX2 -center_x4)+(centerY2 - center_y4)*(centerY2 -center_y4));
        //递归
        if(cen_dis1 <= 0.01||cen_dis2<=0.01){
            return;
        }else{
             cluster1.clear();
             cluster2.clear();
             cluster(list,center_x3,center_x4,center_y3,center_y4);
        }

    }

    //求两个点的欧式距离
    public double getEuclideanDis(Point point1, double centerX,double centerY) {
        double count_dis ;
        double x1 = point1.getX();
        double y1 = point1.getY();

        count_dis = (x1-centerX)*(x1-centerX) + (y1-centerY)*(y1-centerY);
        return Math.sqrt(count_dis);
    }

    //求簇的中心x
    public double CenterX(List<Point> list1){
        double num = 0;
        for(Point point:list1){
            num += point.getX();
        }
        return num / (list1.size());
    }
    //求簇的中心y
    public double CenterY(List<Point> list1){
        double num = 0;
        for(Point point:list1){
            num += point.getY();
        }
        return num / (list1.size());
    }

}
