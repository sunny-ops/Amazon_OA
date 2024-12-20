public class Level {
    private int floor;
    private ParkingSpot[] spots;
    private int availableSpots = 0;
    private static final int SPOTS_PER_ROW = 10;

    public Level(int flr, int numberSpots) {
        floor = flr;
        spots = new ParkingSpot[numberSpots];
        int largeSpots = numberSpots / 4;
        int bikeSpots = numberSpots / 4;
        int compactSpots = numberSpots - largeSpots - bikeSpots;
        for (int i = 0; i < numberSpots; i++) {
            VehicleSize sz = VehicleSize.Motorcycle;
            if(i < largeSpots) {
                sz = VehicleSize.Large;
            } else if (i < largeSpots + compactSpots) {
                sz = VehicleSize.Compact;
            }
            int row = i / SPOTS_PER_ROW;
            spots[i] = new ParkingSpot(this, row, i, sz);
        }
        availableSpots = numberSpots;
    }

    public int getAvailableSpots() {
        return availableSpots;
    }

    public boolean parkVehicle(Vehicle vehicle) {
        if(getAvailableSpots() < vehicle.getSpotsNeeded()) {
            return false;
        }
        int spotNumber = findAvailableSpots(vehicle);
        if(spotNumber < 0) {
            return false;
        }
        return parkStartingAtSpot(spotNumber, vehicle);
    }

    public boolean parkStartingAtSpot(int spotNumber, Vehicle vehicle) {
        vehicle.clearSpots();
        boolean success = true;
        for (int i = spotNumber; i < spotNumber + vehicle.spotsNeed; i++ ){
            success &= spots[i].park(vehicle);
        }
        availableSpots -= vehicle.spotsNeed;
        return success;
    }

    public int findAvailableSpots(Vehicle vehicle) {
        int spotsNeeded = vehicle.getSpotsNeeded();
        int lastRow = -1;
        int spotsFound = 0;
        for (int i = 0; i < spots.length; i++) {
            ParkingSpot spot = spots[i];
            if(lastRow != spot.getRow()){
                spotsFound = 0;
                lastRow = spot.getRow();
            }
            if(spot.canFitVehicle(vehicle)) {
                spotsFound++;
            } else{
                spotsFound = 0;
            }
            if(spotsFound == spotsNeeded) {
                return i - (spotsNeeded - 1);
            }

        }
        return -1;
    }

    public void spotFreed() {
        availableSpots++;
    }
}

