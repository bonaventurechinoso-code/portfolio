
import os
import sys
from datetime import datetime
from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, Response, send_file
from config import Config
from data.portfolio import PROFILE, SKILLS, PROJECTS, EDUCATION, SOCIAL_LINKS

sys.dont_write_bytecode = True


def create_app(config_class=Config):
    """Application factory for the Flask Portfolio Engine."""
    app = Flask(__name__, static_folder="static", template_folder="templates")
    app.config.from_object(config_class)

    # -------------------------------------------------------------------------
    # Route: GET /
    # -------------------------------------------------------------------------
    @app.route("/", methods=["GET"])
    def index():
        """Serve main portfolio page populated with dynamic Python data."""
        return render_template(
            "index.html",
            profile=PROFILE,
            skills=SKILLS,
            projects=PROJECTS,
            education=EDUCATION,
            social_links=SOCIAL_LINKS
        )

    # -------------------------------------------------------------------------
    # Route: GET /health
    # -------------------------------------------------------------------------
    @app.route("/health", methods=["GET"])
    def health():
        """Health check endpoint for service monitoring."""
        return jsonify({"status": "ok"})

    # -------------------------------------------------------------------------
    # Route: GET /favicon.ico
    # -------------------------------------------------------------------------
    @app.route("/favicon.ico", methods=["GET"])
    def favicon():
        """Serve favicon icon to prevent 404 in browser console."""
        return app.send_static_file("images/bonaventure-passport.jpg")

    # -------------------------------------------------------------------------
    # Route: POST /contact
    # -------------------------------------------------------------------------
    @app.route("/contact", methods=["POST"])
    def contact():
        """
        Handle contact submissions:
        - Validates name, email, and message
        - Checks that email contains '@'
        - Saves submission to messages.txt with timestamp
        - Flashes 'Message Sent Successfully'
        - Redirects to /#contact
        """
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        subject = request.form.get("subject", "").strip()
        message = request.form.get("message", "").strip()

        # Validation
        if not name or not email or not message:
            flash("All fields (Name, Email, Message) are required.", "error")
            return redirect(url_for("index") + "#contact")

        if "@" not in email or "." not in email:
            flash("Please enter a valid email address.", "error")
            return redirect(url_for("index") + "#contact")

        # Save to messages.txt
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        record = (
            f"--------------------------------------------------\n"
            f"DATE/TIME: {timestamp}\n"
            f"NAME:      {name}\n"
            f"EMAIL:     {email}\n"
            f"SUBJECT:   {subject if subject else 'N/A'}\n"
            f"MESSAGE:\n{message}\n"
        )

        messages_file = app.config.get("MESSAGES_FILE", "messages.txt")
        try:
            with open(messages_file, "a", encoding="utf-8") as f:
                f.write(record)
        except Exception as e:
            app.logger.error(f"Failed to write to {messages_file}: {e}")
            flash("An error occurred while saving your message. Please try again.", "error")
            return redirect(url_for("index") + "#contact")

        flash("Message Sent Successfully", "success")
        return redirect(url_for("index") + "#contact")

    # -------------------------------------------------------------------------
    # Route: GET /messages
    # -------------------------------------------------------------------------
    @app.route("/messages", methods=["GET"])
    def view_messages():
        """Admin view listing all inquiries recorded in messages.txt."""
        messages_file = app.config.get("MESSAGES_FILE", "messages.txt")
        parsed_messages = []

        if os.path.exists(messages_file):
            try:
                with open(messages_file, "r", encoding="utf-8") as f:
                    content = f.read()

                # Parse records separated by hyphens
                raw_entries = content.split("--------------------------------------------------")
                for entry in raw_entries:
                    lines = [line.strip() for line in entry.strip().splitlines() if line.strip()]
                    if not lines:
                        continue
                    
                    data = {"timestamp": "N/A", "name": "Anonymous", "email": "N/A", "subject": "", "message": ""}
                    msg_body_lines = []
                    is_reading_message = False

                    for line in lines:
                        if line.startswith("DATE/TIME:"):
                            data["timestamp"] = line.replace("DATE/TIME:", "").strip()
                        elif line.startswith("NAME:"):
                            data["name"] = line.replace("NAME:", "").strip()
                        elif line.startswith("EMAIL:"):
                            data["email"] = line.replace("EMAIL:", "").strip()
                        elif line.startswith("SUBJECT:"):
                            data["subject"] = line.replace("SUBJECT:", "").strip()
                        elif line.startswith("MESSAGE:"):
                            is_reading_message = True
                        elif is_reading_message:
                            msg_body_lines.append(line)

                    data["message"] = "\n".join(msg_body_lines)
                    parsed_messages.append(data)
            except Exception as e:
                app.logger.error(f"Error reading messages file: {e}")

        return render_template(
            "messages.html",
            profile=PROFILE,
            messages=parsed_messages
        )

    # -------------------------------------------------------------------------
    # Route: GET /resume (Interactive Resume Preview)
    # -------------------------------------------------------------------------
    @app.route("/resume", methods=["GET"])
    def view_resume():
        """Serve the interactive resume preview page with PDF download and sharing."""
        return render_template(
            "resume.html",
            profile=PROFILE,
            skills=SKILLS,
            projects=PROJECTS,
            education=EDUCATION,
            social_links=SOCIAL_LINKS
        )

    # -------------------------------------------------------------------------
    # Route: GET /resume/pdf (Direct PDF View / Share)
    # -------------------------------------------------------------------------
    @app.route("/resume/pdf", methods=["GET"])
    def view_resume_pdf():
        """Serve the PDF resume inline for in-browser viewing and sharing."""
        pdf_path = os.path.join(app.root_path, "static", "docs", "Bonaventure_Chinonso_Mabia_Resume.pdf")
        if os.path.exists(pdf_path):
            return send_file(
                pdf_path,
                mimetype="application/pdf",
                as_attachment=False
            )
        return redirect(url_for("view_resume"))

    # -------------------------------------------------------------------------
    # Route: GET /download-resume (Downloadable PDF)
    # -------------------------------------------------------------------------
    @app.route("/download-resume", methods=["GET"])
    def download_resume():
        """Serve the official PDF resume file as attachment download."""
        pdf_path = os.path.join(app.root_path, "static", "docs", "Bonaventure_Chinonso_Mabia_Resume.pdf")
        if os.path.exists(pdf_path):
            return send_file(
                pdf_path,
                mimetype="application/pdf",
                as_attachment=True,
                download_name="Bonaventure_Chinonso_Mabia_Resume.pdf"
            )

        # Fallback text format if PDF is unavailable
        resume_text = (
            f"=======================================================\n"
            f"{PROFILE['name'].upper()}\n"
            f"{PROFILE['title']}\n"
            f"Email: {PROFILE['email']} | Timezone: {PROFILE['timezone']}\n"
            f"=======================================================\n\n"
            f"PROFILE SUMMARY:\n{PROFILE['hero_bio']}\n\n"
            f"CORE ARCHITECTURES & PROJECTS:\n"
            f"1. Enterprise Resource & Inventory Management Platform\n"
            f"2. Automated Micro-Deployment & Health Monitoring Agent\n"
            f"3. Distributed Academic Records & Portal System\n"
            f"4. Secure FinTech Transaction Gateway Simulation\n\n"
            f"EDUCATION:\n"
            f"- Higher National Diploma (HND) in Computer Science (Federal Poly Oko)\n"
            f"- National Diploma (ND) in Computer Science (Federal Poly Oko)\n"
            f"- Diploma in Software Engineering (SEDI Nsugbe)\n"
        )
        return Response(
            resume_text,
            mimetype="text/plain",
            headers={"Content-Disposition": "attachment;filename=Bonaventure_Chinonso_Mabia_Resume.txt"}
        )

    # -------------------------------------------------------------------------
    # Error Handlers
    # -------------------------------------------------------------------------
    @app.errorhandler(404)
    def page_not_found(e):
        """Custom 404 error page matching dark theme."""
        return render_template("404.html", profile=PROFILE), 404

    return app


if __name__ == "__main__":
    app = create_app()
    print(f">> Python Portfolio Engine running at http://{Config.HOST}:{Config.PORT}")
    app.run(host=Config.HOST, port=Config.PORT, debug=Config.DEBUG)
