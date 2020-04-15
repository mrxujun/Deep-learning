package com.xujun;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class K_means {
    public static void main(String[] args) {
        Point point1 = new Point(1,1,1);
        Point point2 = new Point(2,2,1);
        Point point3 = new Point(3,1,2);
        Point point4 = new Point(4,2,2);
        Point point5 = new Point(5,4,3);
        Point point6 = new Point(6,5,3);
        Point point7 = new Point(7,4,4);
        Point point8 = new Point(8,5,4);

        List<Point> pointList = new ArrayList<>();
        pointList.add(point1);
        pointList.add(point2);
        pointList.add(point3);
        pointList.add(point4);
        pointList.add(point5);
        pointList.add(point6);
        pointList.add(point7);
        pointList.add(point8);

        Random random = new Random();
        //随机产生两个元素
        Point point_1 = pointList.get(random.nextInt(pointList.size()));
        Point point_2 = pointList.get(random.nextInt(pointList.size()));

        //判断初始的两个点相不相等
        Cluster cluster = new Cluster();
        if(point_1.getId()!= point2.getId()){
            cluster.cluster(pointList,point_1.getX(),point2.getX(),point1.getY(),point2.getY());

        }
        else{
            point_1 = pointList.get(random.nextInt(pointList.size()));
            point_2 = pointList.get(random.nextInt(pointList.size()));
        }
        //打印出每个簇中的元素
        System.out.print("第一个簇：");
        for(Point point:cluster.cluster2){
            System.out.print(point.getId());
        }
        System.out.println();
        System.out.print("第二个簇：");
        for(Point point:cluster.cluster1){
            System.out.print(point.getId());
        }

    }


}
