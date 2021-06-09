/*
Basic functions:

    (Optional)Match making, text messaging, notification

    Recipe/restaurant recommendation ?

    Calories calculation, meal log, intake history visualization

*/

/*
Requirements:

    Fodd data storage (static class, db), Metabolic table (db, api), Person Data( db )

*/

// Base class, implement different roles such as event host by inheritence 
public class Person {

    // Attributes
    public string uuid { get; private set; }
    public string name { get; private set; }
    public string age { get; private set; }
    public string height { get; private set; }
    public string weight { get; private set; }
    public string gender { get; private set; }

    public List<string> friends { get; private set; }
    public List<ActivityGenre> hobbies { get; private set; }
    public HashTable<DailySum> dailyLog { get; private set; } // Hash or independent class or dict

    public float bmi { get; }
    public float baseMetabolic { get; private set; }

    // Methods
    public void FriendRequest () {
        return true;
    }

    public float CaloiesIntakeCal (DateTime startDate = DateTime.ToKday, DateTime endTime = DateTime.Today) {

    }

    public List<Event> GetPotentialInterestEvent(){
        
    }

    public List<Event> GetFriendGoingEvent(){

    }
}



public class Network {
    public HashTable vertices { get; private set; }
}

//////////////////////////////////////////////////////////////////

public class Event {
    // Attribute
    private List < (float, Sport) > _sports;

    public string eventName;
    public Person host;
    public string location { get; private set; }
    public DateTime eventTime { get; private set; }
    public float totalDuration { get; private set }
    public List<Person> participants { get; private set; }
    public int minPlayers { get; private set; }
    public List<ActivityGenre> genres { get; private set; };
    public List < (float, Sport) > sports {
        get {

        }
        set {
            totalDuration = value.ADD (); // Add all sports duration to totalDuration
            genres.AddRange(value.Select(sp=>sp.ActivityGenre));
        }
    }
    public float totalConsumedCalories { get; private set; }

    // Methods

}


public enum ActivityGenre {
    BALL,
    OUTDOORS
}



public class Sport {

    // Attributes
    public ActivityGenre genre { get; }
    public string name { get; private set; }
    public float caloriesBurnedPerHour { get; private set; }
    public float basicContinuousTime { get; }
    public float basicConsume {
        get {
            return caloriesBurnedPerHour * basicContinuousTime;
        }
    }

    // Methods
    public float ConsumedInInterval (float hour) {
        return hour * caloriesBurnedPerHour;
    }
}

//////////////////////////////////////////////////////////////////
pubilc abstrcat class Food {
    public string name { get; private set; }
    public float carbs { get; private set; }
    public float protein { get; private set; }
    public float fat { get; private set; }
    public float calories {
        get {
            return carbs * 4 + protein * 4 + fat * 9;
        }
    }
}

public class Meal {
    public DateTime time { get; private set; } = null;
    public List<Food> inTake { get; private set; }
    public float TotalCalories { get; private set; }

}

public class DailyIntakeCalories {

    // Attributes
    public DateTime date;
    public List<meal> meals {
        get {
            return this.meals;
        }
        set {

        }
    }

    public float TotalCalories { get; private set; }

    // Methods
    public float IntakeTotalCalories () {

    }
}

public class DailyConsumedCalories {
    // Attributes
    public DateTime date;
    public List<Sport> sports {
        get {
            return this.sports;
        }
        set {

        }
    }

    public float TotalCalories { get; private set; }

    // Methods
    public float ConsumedTotalCalories () {

    }
}