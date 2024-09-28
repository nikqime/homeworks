class Animal {
    constructor(name, weight, type, xinkhali) {
        this.name = name;
        this.weight = weight;
        this.type = type;
        this.xinkhali = xinkhali;
    }

    speak() {
        return `${this.xinkhali} ამბობს, რომ იგი არის ${this.xinkhali}`;
    }
}