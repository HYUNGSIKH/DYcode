!C   Modify :    2014/01/12

!  

      dimension num(9000000),xcoord(9000000),ycoord(9000000),
     &depth(9000000)
  
      real(kind=4) frict2manning, frict, g
       
      open(3,file='fort.14',status='old')
      open(4,file='fort.13_quadratic_friction.dat',status='unknown')
      open(5,file='fort.13_mannings_friction.dat',status='unknown')
 
      g=9.80665d0
      
      read(3,*)
      read(3,*)ele,node
      
      write(4,*)'quadratic_friction_coefficient_at_sea_floor'      
      write(4,*)node
      
!      write(5,*)'mannings_n_at_sea_floor'      
!      write(5,*)node      
      do   k=1,node
      read(3,*)num(k),xcoord(k),ycoord(k),depth(k)
  
      frict=0.0
 
!      global
      if(depth(k) .LE. 40.)frict=0.0023
      if(depth(k) .gt. 40. .and. depth(k) .le. 60.)frict=0.0023d0
     &-((depth(k)-40)*(0.0002d0/20.)) !frict=0.020
!    if(depth(k) .gt. 60. .and. depth(k) .le. 200.)frict=0.0025d0-((depth(k)-60)*(0.0002d0/140.))!frict=0.015  
      if(depth(k) .gt. 60.)frict=0.0021
     
!    convert to mannings n     
!     if(depth(k) .le. 0.0)depth(k)=0.0
!     frict2manning=sqrt((frict*(depth(k)**(1.d0/3.d0)))/g )
!     if(depth(k) .le. 0.1)frict2manning=0.0250
      
	    write(4,100)num(k),frict  
!     write(5,100)num(k),frict2manning
      enddo
  
 
  100 format(i10,5x,f8.5) 
  101 format(f8.2,5x,f8.5)  
  
  
      stop
	    end