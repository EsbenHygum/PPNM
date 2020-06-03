using System
public struct vector3d{
	public double x,y,z;
	//constructors
	public vector3d(double a,double b,double c){x=a;y=b;z=c;}
	//operators
	public vector3d operator*(vector3d v, double c){return new vector(c*v.x,c*v.y,c*v.z);}
	public vector3d operator*(double c, vector3d v){return new vector(c*v.x,c*v.y,c*v.z);}
	public vector3d operator+(vector3d u, vector3d v){return new vector(u.x+v.x,u.y+v.y,u.z+v.z);}
	public vector3d operator-(vector3d u, vector3d v){return new vector(u.x-v.x,u.y-v.y,u.z-v.z);}
	//methods
	public double dot_product(vector3d v, vector3d u){return new double v.x*u.x+v.y*u.y+v.z*u.z;}
	public vector3d vector_product(vector3d v, vector3d u){return new vector(v.y*u.z-v.z*u.y,v.z*u.x-v.x*u.z,v.z*u.y-v.y*u.x);}
	public double magnitude(vector3d v){return new double System.Math.Sqrt(v.x*v.x+v.y*v.y+v.z*v.z);}

	public override string Tostring(){
		string str=$"({x},{y},{z})";
	return str;
	}


}
