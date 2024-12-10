// Vehicle,
// - VehicleSize, spotNeeded, parkingSpots, licenseNumber
// ParkingSpot
// - sz, level, row, spotnumber, vehicle
// Level
// - an array of parkingspots, floor, available spots, NUM_EACH_ROW
// Parking Lot
// - an array of Levels, capacity, NUM_OF_LEVELS
// Ticket
// - vehicle, timestamp

public enum VehicleSize {
    Compact,
    Large,
    Motorcycle
}

public abstract class Vehicle {
    protected VehicleSize vs;
    protected int spotNeeded;
    protected List<ParkingSpot> parkingSpots = new ArrayList<ParkingSpot>;
    protected String licenseNumber;

    public getSpotNeeded(){
        return this.spotNeeded;
    }

    public void parkInSpot(ParkingSpot parkingSpot) {
        parkingSpots.add(parkingSpot);
    }

    public void clearSpot() {
        for (int i = 0; i < parkingSpots.size(); i++) {
            parkingSpots.get(i).removeVehicle();
        }
        parkingSpots.clear();
    }

    public abstract boolean canFitIn(ParkingSpot spot);
    }

}

public class Car extends Vehicle {
    public Car {
        spotNeeded = 1;
        vs = VehicleSize.Compact;
    }

    public boolean canFitIn(ParkingSpot spot) {
        return spot.getSize() == VehicleSize.Compact || spot.getSize() == VehicleSize.Large;
    }
}

public class Bus extends Vehicle {
    public Bus {
        spotNeeded = 5;
        vs = VehicleSize.Large;
    }

    public boolean canFitIn(ParkingSpot spot) {
        return spot.getSize == VehicleSize.Large;
    }
}

public class ParkingSpot {
    private VehicleSize vs;
    private Level lvl;
    private int row;
    private Vehicle vehicle;
    private int spotnumber;

    public ParkingSpot (Level lvl, int r, int n, Vehicle v){
        vehicle = v;
        lvl = lvl;
        row = r;
        spotnumber = n;
    }

    public boolean isAvailable() {
        return vehicle == null;
    }

    public boolean canFitVehicle(Vehicle ve) {
        return ve.canFitIn(this);
    }

    public boolean park(Vehicle ve) {
        if (!canFitVehicle(ve)) {
            return false;
        }
        vehicle = ve;
        ve.parkInSpot(this);
        return true;
    }

    public boolean removeVehicle() {
        vehicle = null;
        levle.spotFree();
    }
}

public class Level {
    private List<ParkingSpot> parkingspots = new ArrayList<ParkingSpot>;
    private int availablespots;
    private static final int NUM_EACH_ROW;
    private int floor;
    
    public Level(int flr, int numberSpots){
        floor = flr;
        spots = new ParkingSpot[numberSpots];
        // ...
    }

    public getAvailableSpot() {
        return availablespots;
    }

    public boolean parkVehicle(Vehicle vehicle) {
        if (getAvailableSpot() < vehicle.getSpotNeeded()) {
            return false;
        }
        int spotNumber = findSpotNumber(vehicle);
        return parkStaringAtSpot(vehicle, spotNumber);
    }

    public parkStartingAtSpot(Vehicle ve, int spotNumber) {
        for (int i = 0; i < ve.getSpotNeeded(); i++) {
            parkingspots[i].park(vehicle);
        }
    }


}