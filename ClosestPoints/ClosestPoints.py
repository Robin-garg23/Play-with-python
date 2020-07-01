"""
CSE101: Introduction to Programming
Assignment 3

Name        : Robin Garg
Roll-no     : 2019092
"""



import math
import random



def dist(p1, p2):
    """
    Find the euclidean distance between two 2-D points

    Args:
        p1: (p1_x, p1_y)
        p2: (p2_x, p2_y)
    
    Returns:
        Euclidean distance between p1 and p2
    """
    d=((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5
    
    return d



def sort_points_by_X(points):
    """
    Sort a list of points by their X coordinate

    Args:
        points: List of points [(p1_x, p1_y), (p2_x, p2_y), ...]
    
    Returns:
        List of points sorted by X coordinate
    """
    for i in range(len(points)):
        d=points[i]
        for j in range(i,len(points)):
            if (d[0]>points[j][0]):
                    d=points[j]
                    points[j]=points[i]
                    points[i]=d
        
    return points
    



def sort_points_by_Y(points):
    """
    Sort a list of points by their Y coordinate

    Args:
        points: List of points [(p1_x, p1_y), (p2_x, p2_y), ...]
    
    Returns:
        List of points sorted by Y coordinate 
    """
    for i in range(len(points)):
        d=points[i]
        for j in range(i,len(points)):
            if (d[1]>points[j][1]):
                    d=points[j]
                    points[j]=points[i]
                    points[i]=d
        
    return points



def naive_closest_pair(plane):
    """
    Find the closest pair of points in the plane using the brute
    force approach

    Args:
        plane: List of points [(p1_x, p1_y), (p2_x, p2_y), ...]

    Returns:
        Distance between closest pair of points and closest pair 
        of points: [dist_bw_p1_p2, (p1_x, p1_y), (p2_x, p2_y)]
    """
    if len(plane)==1:
        return plane
    a=[dist(plane[0],plane[1]),plane[0],plane[1]]
    
    for i in range(len(plane)):
        for j in range(len(plane)):
            if i!=j:
                e=dist(plane[i],plane[j])
                if a[0]>e:
                    a[0]=e
                    a[1]=plane[i]
                    a[2]=plane[j]
    return a
            
                    
            



def closest_pair_in_strip(points, d):
    """
    Find the closest pair of points in the given strip with a 
    given upper bound. This function is called by 
    efficient_closest_pair_routine

    Args:
        points: List of points in the strip of interest.
        d: Minimum distance already found found by 
            efficient_closest_pair_routine

    Returns:
        Distance between closest pair of points and closest pair 
        of points: [dist_bw_p1_p2, (p1_x, p1_y), (p2_x, p2_y)] if
        distance between p1 and p2 is less than d. Otherwise
        return -1.
    """
    points=sort_points_by_Y(points)
    if len(points)==1:
        return -1
    a=[dist(points[0],points[1]),points[0],points[1]]
    
    for i in range(len(points)):
        if i+6<=len(points):
            s=i+6
        else:
            s=len(points)
        for j in range(i+1,s):
            e=dist(points[i],points[j])
            if a[0]>e:
                a[0]=e
                a[1]=points[i]
                a[2]=points[j]
    if a[0]>=d:
        return -1
    else:
        return a


def efficient_closest_pair_routine(points):
    """
    This routine calls itself recursivly to find the closest pair of
    points in the plane. 

    Args:
        points: List of points sorted by X coordinate

    Returns:
        Distance between closest pair of points and closest pair 
        of points: [dist_bw_p1_p2, (p1_x, p1_y), (p2_x, p2_y)]
    """
    
    a=len(points)//2
    mid=points[a]
    if len(points)==1:
        return points
    if len(points)==2:
        d=dist(points[0],points[1])
        return [d]+points
    
    r1=efficient_closest_pair_routine(points[0:a])
    r2=efficient_closest_pair_routine(points[a:])
    if type(r1[0])==tuple:
        r=r2
        d=r2[0]
    else:
        if r1[0]<=r2[0]:
            r=r1
            d=r1[0]
        elif r1[0]>r2[0]:
            r=r2
            d=r2[0]
    pnt=[]
    for i in range(len(points)):
        if abs(mid[0]-points[i][0])<=d:
            pnt.append(points[i])
    r_strip=closest_pair_in_strip(pnt, d)
    if type(r_strip)==int:
        return r
    else:
        return r_strip


def efficient_closest_pair(points):
    """
    Find the closest pair of points in the plane using the divide
    and conquer approach by calling efficient_closest_pair_routine.

    Args:
        plane: List of points [(p1_x, p1_y), (p2_x, p2_y), ...]

    Returns:
        Distance between closest pair of points and closest pair 
        of points: [dist_bw_p1_p2, (p1_x, p1_y), (p2_x, p2_y)]
    """
    points=sort_points_by_X(points)
    return efficient_closest_pair_routine(points)
     



def generate_plane(plane_size, num_pts):
    """
    Function to generate random points.

    Args:
        plane_size: Size of plane (X_max, Y_max)
        num_pts: Number of points to generate

    Returns:
        List of random points: [(p1_x, p1_y), (p2_x, p2_y), ...]
    """
    
    gen = random.sample(range(plane_size[0]*plane_size[1]), num_pts)
    random_points = [(i%plane_size[0] + 1, i//plane_size[1] + 1) for i in gen]

    return random_points



if __name__ == "__main__":  
    #number of points to generate
    num_pts = 10
    #size of plane for generation of points
    plane_size = (100, 100) 
    plane = generate_plane(plane_size, num_pts)
    #print(plane)
    #naive_closest_pair(plane)
    #efficient_closest_pair(plane)
