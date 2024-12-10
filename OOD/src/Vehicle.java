import java.util.ArrayList;

public abstract class Vehicle {
    protected ArrayList<ParkingSpot> parkingSpots = new ArrayList<ParkingSpot>();
    protected String licensePlate;
    protected int spotsNeed;
    protected VehicleSize size;

    public int getSpotsNeeded() {
        return spotsNeed;
    }

    public VehicleSize getSize() {
        return size;
    }

    public void parkInSpot(ParkingSpot spot) {
        parkingSpots.add(spot);
    }

    public void clearSpots() {
        for (int i = 0; i < parkingSpots.size(); i++ ) {
            parkingSpots.get(i).removeVehicle();
        }
        parkingSpots.clear();
    }

    public  abstract  boolean canFitInSpot(ParkingSpot spot);
    public  abstract void print();

}


