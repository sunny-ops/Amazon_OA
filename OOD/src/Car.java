public class Car extends Vehicle{
    public Car() {
        spotsNeed = 1;
        size = VehicleSize.Compact;
    }

    public boolean canFitInSpot(ParkingSpot spot) {
        return spot.getSize() == VehicleSize.Large || spot.getSize() == VehicleSize.Compact;
    }

    public  void print() {
        System.out.println("C");
    }
}
