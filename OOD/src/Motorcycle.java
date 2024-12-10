public class Motorcycle extends Vehicle{
    public Motorcycle() {
        spotsNeed = 1;
        size = VehicleSize.Motorcycle;
    }

    @Override
    public boolean canFitInSpot(ParkingSpot spot) {
        return true;
    }

    @Override
    public void print() {
        System.out.println("M");
    }
}
