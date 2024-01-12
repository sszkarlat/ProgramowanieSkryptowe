/**
 * @author Stanisław Polak <polak@agh.edu.pl>
 */

// @deno-types="npm:@types/express@^4"
import express, { Express, Request, Response } from "npm:express@^4";
import morgan from "npm:morgan@^1";
import "npm:pug@^3";

const app: Express = express();

// Poprawiono tą linię
let deno_logo : string =
  "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Deno_2021.svg/120px-Deno_2021.svg.png";

app.set("view engine", "pug");
app.locals.pretty = app.get("env") === "development";

app.use(morgan("dev"));
app.use(express.urlencoded({ extended: false }));

// Tutaj poprawiłem Request oraz Response
app.get("/", function (_req: Request, res: Response) {
  res.render("index", { deno_logo });
});

// Tutaj poprawiłem Request oraz Response oraz dopisałem void
app.post("/", function (req: Request, res: Response): void {
  res.send(`Hello '${req.body.name}'`);
});

app.listen(8000, function () {
  console.log("The application is available on port 8000");
});
