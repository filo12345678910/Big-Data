class Movie {
  final String title;
  final int duration;
  final List<String> genres;
  final double rating;

  Movie({
    required this.title,
    required this.duration,
    required this.genres,
    required this.rating,
  });
}

class Seat {
  final int X;
  final int Y;
  bool isReserved = false;

  Seat({required this.X, required this.Y, this.isReserved = false});
}

class CinemaRoom {
  final String name;
  final List<Seat> seats;

  CinemaRoom({
    required this.name,
    required this.seats,
  });
}

class MovieShow {
  final String uuid;
  final Movie movie;
  final String cinemaRoomUuid;
  final DateTime showTime;

  MovieShow({
    required this.uuid,
    required this.movie,
    required this.cinemaRoomUuid,
    required this.showTime,
  });
}
