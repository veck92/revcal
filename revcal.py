def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a number greater than zero.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def get_non_empty_string(prompt):
    while True:
        value = input(prompt).strip()
        if value == "":
            print("This field cannot be empty.")
        else:
            return value


def main():
    print("=== Revenue Tax Split Calculator ===\n")

    # Step 1: Basic info
    num_jobs = int(get_positive_number(
        "Insert how many jobs you currently have: "))
    tax_credits = get_positive_number(
        "Insert your current annual tax credits (€): ")
    annual_income = get_positive_number(
        "Insert your total annual income (€): ")

    print("\n--- Insert information for each job ---")
    jobs = []

    for i in range(1, num_jobs + 1):
        print(f"\nJob #{i}")
        company_name = get_non_empty_string("Insert the name of the company: ")
        hours_per_week = get_positive_number(
            "Insert how many hours you work at this company weekly: ")
        salary_per_hour = get_positive_number(
            "Insert your salary per hour (€): ")

        annual_job_income = hours_per_week * salary_per_hour * 52  # Estimated income

        job_info = {
            "company_name": company_name,
            "hours_per_week": hours_per_week,
            "salary_per_hour": salary_per_hour,
            "estimated_annual_income": annual_job_income
        }

        jobs.append(job_info)

    # Step 2: Calculate proportional values
    total_estimated_income = sum(
        job["estimated_annual_income"] for job in jobs)

    print("\n--- Proportional Allocation ---")
    for job in jobs:
        proportion = job["estimated_annual_income"] / total_estimated_income
        allocated_income = annual_income * proportion
        allocated_credits = tax_credits * proportion

        print(f"\nCompany: {job['company_name']}")
        print(
            f"Estimated annual income from this job: €{job['estimated_annual_income']:.2f}")
        print(f"Proportion of total income: {proportion:.2%}")
        print(f"Allocated annual income: €{allocated_income:.2f}")
        print(f"Allocated tax credits: €{allocated_credits:.2f}")


if __name__ == "__main__":
    main()
# This script calculates the proportional allocation of annual income and tax credits
# based on the estimated income from multiple jobs.
